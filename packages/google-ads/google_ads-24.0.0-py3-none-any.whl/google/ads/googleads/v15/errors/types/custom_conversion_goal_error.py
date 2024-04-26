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
        "CustomConversionGoalErrorEnum",
    },
)


class CustomConversionGoalErrorEnum(proto.Message):
    r"""Container for enum describing possible custom conversion goal
    errors.

    """

    class CustomConversionGoalError(proto.Enum):
        r"""Enum describing possible custom conversion goal errors."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_CONVERSION_ACTION = 2
        CONVERSION_ACTION_NOT_ENABLED = 3
        CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL = 4
        CUSTOM_GOAL_DUPLICATE_NAME = 5
        DUPLICATE_CONVERSION_ACTION_LIST = 6
        NON_BIDDABLE_CONVERSION_ACTION_NOT_ELIGIBLE_FOR_CUSTOM_GOAL = 7


__all__ = tuple(sorted(__protobuf__.manifest))
