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
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class IntOrSympy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INT_VAL_FIELD_NUMBER: builtins.int
    SYMPY_EXPR_FIELD_NUMBER: builtins.int
    int_val: builtins.int
    sympy_expr: builtins.str
    def __init__(
        self,
        *,
        int_val: builtins.int = ...,
        sympy_expr: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["int_val", b"int_val", "sympy_expr", b"sympy_expr", "val", b"val"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["int_val", b"int_val", "sympy_expr", b"sympy_expr", "val", b"val"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["val", b"val"]) -> typing_extensions.Literal["int_val", "sympy_expr"] | None: ...

global___IntOrSympy = IntOrSympy

@typing_extensions.final
class NDArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NDARRAY_FIELD_NUMBER: builtins.int
    ndarray: builtins.bytes
    """A Numpy array serialized as bytes using np.save() / np.load()."""
    def __init__(
        self,
        *,
        ndarray: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ndarray", b"ndarray"]) -> None: ...

global___NDArray = NDArray

@typing_extensions.final
class Complex(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REAL_FIELD_NUMBER: builtins.int
    IMAG_FIELD_NUMBER: builtins.int
    real: builtins.float
    imag: builtins.float
    def __init__(
        self,
        *,
        real: builtins.float = ...,
        imag: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["imag", b"imag", "real", b"real"]) -> None: ...

global___Complex = Complex
