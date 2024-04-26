#  Copyright 2023 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import Union

import numpy as np
import sympy
from cirq._doc import document

SymbolicFloat = Union[float, sympy.Expr]
document(SymbolicFloat, """A floating point value or a sympy expression.""")

SymbolicInt = Union[int, sympy.Expr]
document(SymbolicFloat, """A floating point value or a sympy expression.""")


def is_symbolic(*args) -> bool:
    return any(isinstance(x, sympy.Basic) for x in args)


def pi(*args) -> SymbolicFloat:
    return sympy.pi if is_symbolic(*args) else np.pi


def log2(x: SymbolicFloat) -> SymbolicFloat:
    from sympy.codegen.cfunctions import log2

    if not isinstance(x, sympy.Basic):
        return np.log2(x)
    return log2(x)


def ceil(x: SymbolicFloat) -> SymbolicInt:
    if not isinstance(x, sympy.Basic):
        return int(np.ceil(x))
    return sympy.ceiling(x)


def floor(x: SymbolicFloat) -> SymbolicInt:
    if not isinstance(x, sympy.Basic):
        return int(np.floor(x))
    return sympy.floor(x)


def bit_length(x: SymbolicFloat) -> SymbolicInt:
    """Returns the number of bits required to represent the integer part of positive float `x`."""
    if not is_symbolic(x) and 0 <= x < 1:
        return 0
    ret = ceil(log2(x))
    if is_symbolic(ret):
        return ret
    return ret + 1 if ret == floor(log2(x)) else ret


def smax(*args):
    if any(isinstance(arg, sympy.Basic) for arg in args):
        return sympy.Max(*args)
    return max(*args)


def acos(x: SymbolicFloat) -> SymbolicFloat:
    if not isinstance(x, sympy.Basic):
        return np.arccos(x)
    return sympy.acos(x)
