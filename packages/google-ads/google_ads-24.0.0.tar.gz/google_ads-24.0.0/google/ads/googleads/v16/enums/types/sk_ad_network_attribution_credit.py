# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
#
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v16.enums",
    marshal="google.ads.googleads.v16",
    manifest={
        "SkAdNetworkAttributionCreditEnum",
    },
)


class SkAdNetworkAttributionCreditEnum(proto.Message):
    r"""Container for enumeration of SkAdNetwork attribution credits."""

    class SkAdNetworkAttributionCredit(proto.Enum):
        r"""Enumerates SkAdNetwork attribution credits."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        WON = 3
        CONTRIBUTED = 4


__all__ = tuple(sorted(__protobuf__.manifest))
