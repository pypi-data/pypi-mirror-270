"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Copyright 2023 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import qualtran.protos.args_pb2
import qualtran.protos.data_types_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Register(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Side:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SideEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Register._Side.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: Register._Side.ValueType  # 0
        LEFT: Register._Side.ValueType  # 1
        RIGHT: Register._Side.ValueType  # 2
        THRU: Register._Side.ValueType  # 3

    class Side(_Side, metaclass=_SideEnumTypeWrapper):
        """A quantum register."""

    UNKNOWN: Register.Side.ValueType  # 0
    LEFT: Register.Side.ValueType  # 1
    RIGHT: Register.Side.ValueType  # 2
    THRU: Register.Side.ValueType  # 3

    NAME_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    SIDE_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def dtype(self) -> qualtran.protos.data_types_pb2.QDataType: ...
    @property
    def shape(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[qualtran.protos.args_pb2.IntOrSympy]: ...
    side: global___Register.Side.ValueType
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        dtype: qualtran.protos.data_types_pb2.QDataType | None = ...,
        shape: collections.abc.Iterable[qualtran.protos.args_pb2.IntOrSympy] | None = ...,
        side: global___Register.Side.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dtype", b"dtype"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dtype", b"dtype", "name", b"name", "shape", b"shape", "side", b"side"]) -> None: ...

global___Register = Register

@typing_extensions.final
class Registers(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTERS_FIELD_NUMBER: builtins.int
    @property
    def registers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Register]:
        """A collection of Registers."""
    def __init__(
        self,
        *,
        registers: collections.abc.Iterable[global___Register] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["registers", b"registers"]) -> None: ...

global___Registers = Registers
