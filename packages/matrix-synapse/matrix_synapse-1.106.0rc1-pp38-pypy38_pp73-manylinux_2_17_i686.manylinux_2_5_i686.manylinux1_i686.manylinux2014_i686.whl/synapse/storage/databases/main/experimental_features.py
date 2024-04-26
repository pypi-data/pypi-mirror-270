#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright 2023 The Matrix.org Foundation C.I.C
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

from typing import TYPE_CHECKING, Dict, FrozenSet, List, Tuple, cast

from synapse.storage.database import DatabasePool, LoggingDatabaseConnection
from synapse.storage.databases.main import CacheInvalidationWorkerStore
from synapse.util.caches.descriptors import cached

if TYPE_CHECKING:
    from synapse.rest.admin.experimental_features import ExperimentalFeature
    from synapse.server import HomeServer


class ExperimentalFeaturesStore(CacheInvalidationWorkerStore):
    def __init__(
        self,
        database: DatabasePool,
        db_conn: LoggingDatabaseConnection,
        hs: "HomeServer",
    ) -> None:
        super().__init__(database, db_conn, hs)

    @cached()
    async def list_enabled_features(self, user_id: str) -> FrozenSet[str]:
        """
        Checks to see what features are enabled for a given user
        Args:
            user:
                the user to be queried on
        Returns:
            the features currently enabled for the user
        """
        enabled = cast(
            List[Tuple[str]],
            await self.db_pool.simple_select_list(
                table="per_user_experimental_features",
                keyvalues={"user_id": user_id, "enabled": True},
                retcols=("feature",),
            ),
        )

        return frozenset(feature[0] for feature in enabled)

    async def set_features_for_user(
        self,
        user: str,
        features: Dict["ExperimentalFeature", bool],
    ) -> None:
        """
        Enables or disables features for a given user
        Args:
            user:
                the user for whom to enable/disable the features
            features:
                pairs of features and True/False for whether the feature should be enabled
        """
        for feature, enabled in features.items():
            await self.db_pool.simple_upsert(
                table="per_user_experimental_features",
                keyvalues={"feature": feature, "user_id": user},
                values={"enabled": enabled},
                insertion_values={"user_id": user, "feature": feature},
            )

            await self.invalidate_cache_and_stream("list_enabled_features", (user,))
