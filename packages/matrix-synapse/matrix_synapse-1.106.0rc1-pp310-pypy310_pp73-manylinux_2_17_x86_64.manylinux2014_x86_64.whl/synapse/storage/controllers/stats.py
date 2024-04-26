#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright 2023 The Matrix.org Foundation C.I.C.
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

import logging
from typing import TYPE_CHECKING, Collection, Counter, List, Tuple

from synapse.api.errors import SynapseError
from synapse.storage.database import LoggingTransaction
from synapse.storage.databases import Databases
from synapse.storage.engines import PostgresEngine

if TYPE_CHECKING:
    from synapse.server import HomeServer

logger = logging.getLogger(__name__)


class StatsController:
    """High level interface for getting statistics."""

    def __init__(self, hs: "HomeServer", stores: Databases):
        self.stores = stores

    async def get_room_db_size_estimate(self) -> List[Tuple[str, int]]:
        """Get an estimate of the largest rooms and how much database space they
        use, in bytes.

        Only works against PostgreSQL.

        Note: this uses the postgres statistics so is a very rough estimate.
        """

        # Note: We look at both tables on the main and state databases.
        if not isinstance(self.stores.main.database_engine, PostgresEngine):
            raise SynapseError(400, "Endpoint requires using PostgreSQL")

        if not isinstance(self.stores.state.database_engine, PostgresEngine):
            raise SynapseError(400, "Endpoint requires using PostgreSQL")

        # For each "large" table, we go through and get the largest rooms
        # and an estimate of how much space they take. We can then sum the
        # results and return the top 10.
        #
        # This isn't the most accurate, but given all of these are estimates
        # anyway its good enough.
        room_estimates: Counter[str] = Counter()

        # Return size of the table on disk, including indexes and TOAST.
        table_sql = """
            SELECT pg_total_relation_size(?)
        """

        # Get an estimate for the largest rooms and their frequency.
        #
        # Note: the cast here is a hack to cast from `anyarray` to an actual
        # type. This ensures that psycopg2 passes us a back a a Python list.
        column_sql = """
            SELECT
                most_common_vals::TEXT::TEXT[], most_common_freqs::TEXT::NUMERIC[]
            FROM pg_stats
            WHERE tablename = ? and attname = 'room_id'
        """

        def get_room_db_size_estimate_txn(
            txn: LoggingTransaction,
            tables: Collection[str],
        ) -> None:
            for table in tables:
                txn.execute(table_sql, (table,))
                row = txn.fetchone()
                assert row is not None
                (table_size,) = row

                txn.execute(column_sql, (table,))
                row = txn.fetchone()
                assert row is not None
                vals, freqs = row

                for room_id, freq in zip(vals, freqs):
                    room_estimates[room_id] += int(freq * table_size)

        await self.stores.main.db_pool.runInteraction(
            "get_room_db_size_estimate_main",
            get_room_db_size_estimate_txn,
            (
                "event_json",
                "events",
                "event_search",
                "event_edges",
                "event_push_actions",
                "stream_ordering_to_exterm",
            ),
        )

        await self.stores.state.db_pool.runInteraction(
            "get_room_db_size_estimate_state",
            get_room_db_size_estimate_txn,
            ("state_groups_state",),
        )

        return room_estimates.most_common(10)
