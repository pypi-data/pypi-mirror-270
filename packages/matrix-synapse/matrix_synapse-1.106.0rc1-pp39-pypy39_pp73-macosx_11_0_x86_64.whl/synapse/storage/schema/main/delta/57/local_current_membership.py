#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright (C) 2023 New Vector, Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# See the GNU Affero General Public License for more details:
# <https://www.gnu.org/licenses/agpl-3.0.html>.
#
# Originally licensed under the Apache License, Version 2.0:
# <http://www.apache.org/licenses/LICENSE-2.0>.
#
# [This file includes modifications made by New Vector Limited]
#
#


# We create a new table called `local_current_membership` that stores the latest
# membership state of local users in rooms, which helps track leaves/bans/etc
# even if the server has left the room (and so has deleted the room from
# `current_state_events`). This will also include outstanding invites for local
# users for rooms the server isn't in.
#
# If the server isn't and hasn't been in the room then it will only include
# outsstanding invites, and not e.g. pre-emptive bans of local users.
#
# If the server later rejoins a room `local_current_membership` can simply be
# replaced with the new current state of the room (which results in the
# equivalent behaviour as if the server had remained in the room).


from synapse.config.homeserver import HomeServerConfig
from synapse.storage.database import LoggingTransaction
from synapse.storage.engines import BaseDatabaseEngine


def run_upgrade(
    cur: LoggingTransaction,
    database_engine: BaseDatabaseEngine,
    config: HomeServerConfig,
) -> None:
    # We need to do the insert in `run_upgrade` section as we don't have access
    # to `config` in `run_create`.

    # This upgrade may take a bit of time for large servers (e.g. one minute for
    # matrix.org) but means we avoid a lots of book keeping required to do it as
    # a background update.

    # We check if the `current_state_events.membership` is up to date by
    # checking if the relevant background update has finished. If it has
    # finished we can avoid doing a join against `room_memberships`, which
    # speesd things up.
    cur.execute(
        """SELECT 1 FROM background_updates
            WHERE update_name = 'current_state_events_membership'
        """
    )
    current_state_membership_up_to_date = not bool(cur.fetchone())

    # Cheekily drop and recreate indices, as that is faster.
    cur.execute("DROP INDEX local_current_membership_idx")
    cur.execute("DROP INDEX local_current_membership_room_idx")

    if current_state_membership_up_to_date:
        sql = """
            INSERT INTO local_current_membership (room_id, user_id, event_id, membership)
                SELECT c.room_id, state_key AS user_id, event_id, c.membership
                FROM current_state_events AS c
                WHERE type = 'm.room.member' AND c.membership IS NOT NULL AND state_key LIKE ?
        """
    else:
        # We can't rely on the membership column, so we need to join against
        # `room_memberships`.
        sql = """
            INSERT INTO local_current_membership (room_id, user_id, event_id, membership)
                SELECT c.room_id, state_key AS user_id, event_id, r.membership
                FROM current_state_events AS c
                INNER JOIN room_memberships AS r USING (event_id)
                WHERE type = 'm.room.member' AND state_key LIKE ?
        """
    cur.execute(sql, ("%:" + config.server.server_name,))

    cur.execute(
        "CREATE UNIQUE INDEX local_current_membership_idx ON local_current_membership(user_id, room_id)"
    )
    cur.execute(
        "CREATE INDEX local_current_membership_room_idx ON local_current_membership(room_id)"
    )


def run_create(cur: LoggingTransaction, database_engine: BaseDatabaseEngine) -> None:
    cur.execute(
        """
        CREATE TABLE local_current_membership (
            room_id TEXT NOT NULL,
            user_id TEXT NOT NULL,
            event_id TEXT NOT NULL,
            membership TEXT NOT NULL
        )"""
    )

    cur.execute(
        "CREATE UNIQUE INDEX local_current_membership_idx ON local_current_membership(user_id, room_id)"
    )
    cur.execute(
        "CREATE INDEX local_current_membership_room_idx ON local_current_membership(room_id)"
    )
