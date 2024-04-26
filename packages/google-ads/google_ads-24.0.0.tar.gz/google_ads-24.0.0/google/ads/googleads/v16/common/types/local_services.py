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
    package="google.ads.googleads.v16.common",
    marshal="google.ads.googleads.v16",
    manifest={
        "LocalServicesDocumentReadOnly",
    },
)


class LocalServicesDocumentReadOnly(proto.Message):
    r"""A Local Services Document with read only accessible data.
    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        document_url (str):
            URL to access an already uploaded Local
            Services document.

            This field is a member of `oneof`_ ``_document_url``.
    """

    document_url: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
