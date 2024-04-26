# Copyright 2023 The Matrix.org Foundation C.I.C.
# Copyright 2023 The Matrix.org Foundation C.I.C.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List

class ServerAclEvaluator:
    def __init__(
        self, allow_ip_literals: bool, allow: List[str], deny: List[str]
    ) -> None: ...
    def server_matches_acl_event(self, server_name: str) -> bool: ...
