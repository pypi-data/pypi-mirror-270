#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright 2022 The Matrix.org Foundation C.I.C.
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


from abc import ABC, abstractmethod
from typing import Iterable

from prometheus_client import Metric

try:
    from prometheus_client.registry import Collector
except ImportError:
    # prometheus_client.Collector is new as of prometheus 0.14. We redefine it here
    # for compatibility with earlier versions.
    class _Collector(ABC):
        @abstractmethod
        def collect(self) -> Iterable[Metric]:
            pass

    Collector = _Collector  # type: ignore
