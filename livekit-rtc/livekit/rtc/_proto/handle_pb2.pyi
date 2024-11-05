"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2023 LiveKit, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class FfiOwnedHandle(google.protobuf.message.Message):
    """# Safety
    The foreign language is responsible for disposing handles
    Forgetting to dispose the handle may lead to memory leaks

    Dropping a handle doesn't necessarily mean that the object is destroyed if it is still used
    on the FfiServer (Atomic reference counting)

    When referring to a handle without owning it, we just use an uint32 without this message.
    (the variable name is suffixed with "_handle")
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.int
    def __init__(
        self,
        *,
        id: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___FfiOwnedHandle = FfiOwnedHandle
