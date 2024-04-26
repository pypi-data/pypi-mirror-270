# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
    package="google.ads.googleads.v15.errors",
    marshal="google.ads.googleads.v15",
    manifest={
        "FeedItemSetErrorEnum",
    },
)


class FeedItemSetErrorEnum(proto.Message):
    r"""Container for enum describing possible feed item set errors."""

    class FeedItemSetError(proto.Enum):
        r"""Enum describing possible feed item set errors."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ITEM_SET_REMOVED = 2
        CANNOT_CLEAR_DYNAMIC_FILTER = 3
        CANNOT_CREATE_DYNAMIC_FILTER = 4
        INVALID_FEED_TYPE = 5
        DUPLICATE_NAME = 6
        WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE = 7
        DYNAMIC_FILTER_INVALID_CHAIN_IDS = 8


__all__ = tuple(sorted(__protobuf__.manifest))
