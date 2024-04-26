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
from typing import TYPE_CHECKING, Dict, Optional

from synapse._pydantic_compat import HAS_PYDANTIC_V2

if TYPE_CHECKING or HAS_PYDANTIC_V2:
    from pydantic.v1 import Extra, StrictInt, StrictStr, constr, validator
else:
    from pydantic import Extra, StrictInt, StrictStr, constr, validator

from synapse.rest.models import RequestBodyModel
from synapse.util.threepids import validate_email


class AuthenticationData(RequestBodyModel):
    """
    Data used during user-interactive authentication.

    (The name "Authentication Data" is taken directly from the spec.)

    Additional keys will be present, depending on the `type` field. Use
    `.dict(exclude_unset=True)` to access them.
    """

    class Config:
        extra = Extra.allow

    session: Optional[StrictStr] = None
    type: Optional[StrictStr] = None


if TYPE_CHECKING:
    ClientSecretStr = StrictStr
else:
    # See also assert_valid_client_secret()
    ClientSecretStr = constr(
        regex="[0-9a-zA-Z.=_-]",  # noqa: F722
        min_length=1,
        max_length=255,
        strict=True,
    )


class ThreepidRequestTokenBody(RequestBodyModel):
    client_secret: ClientSecretStr
    id_server: Optional[StrictStr]
    id_access_token: Optional[StrictStr]
    next_link: Optional[StrictStr]
    send_attempt: StrictInt

    @validator("id_access_token", always=True)
    def token_required_for_identity_server(
        cls, token: Optional[str], values: Dict[str, object]
    ) -> Optional[str]:
        if values.get("id_server") is not None and token is None:
            raise ValueError("id_access_token is required if an id_server is supplied.")
        return token


class EmailRequestTokenBody(ThreepidRequestTokenBody):
    email: StrictStr

    # Canonicalise the email address. The addresses are all stored canonicalised
    # in the database. This allows the user to reset his password without having to
    # know the exact spelling (eg. upper and lower case) of address in the database.
    # Without this, an email stored in the database as "foo@bar.com" would cause
    # user requests for "FOO@bar.com" to raise a Not Found error.
    _email_validator = validator("email", allow_reuse=True)(validate_email)


if TYPE_CHECKING:
    ISO3116_1_Alpha_2 = StrictStr
else:
    # Per spec: two-letter uppercase ISO-3166-1-alpha-2
    ISO3116_1_Alpha_2 = constr(regex="[A-Z]{2}", strict=True)


class MsisdnRequestTokenBody(ThreepidRequestTokenBody):
    country: ISO3116_1_Alpha_2
    phone_number: StrictStr
