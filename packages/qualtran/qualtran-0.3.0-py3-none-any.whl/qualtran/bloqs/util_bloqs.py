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

"""Bloqs for virtual operations and register reshaping."""

from functools import cached_property
from typing import Any, Dict, Iterable, Optional, Sequence, Set, Tuple, TYPE_CHECKING, Union

import attrs
import numpy as np
import quimb.tensor as qtn
from attrs import frozen
from sympy import Expr

from qualtran import (
    Bloq,
    BloqBuilder,
    GateWithRegisters,
    QAny,
    QBit,
    QDType,
    Register,
    Side,
    Signature,
    Soquet,
    SoquetT,
)
from qualtran.cirq_interop.t_complexity_protocol import TComplexity
from qualtran.drawing import directional_text_box, WireSymbol
from qualtran.resource_counting.symbolic_counting_utils import SymbolicInt
from qualtran.simulation.classical_sim import bits_to_ints, ints_to_bits

if TYPE_CHECKING:
    from numpy.typing import NDArray

    from qualtran import AddControlledT, CtrlSpec
    from qualtran.cirq_interop import CirqQuregT
    from qualtran.resource_counting import BloqCountT, SympySymbolAllocator
    from qualtran.simulation.classical_sim import ClassicalValT


@frozen
class Split(Bloq):
    """Split a bitsize `n` register into a length-`n` array-register.

    Attributes:
        dtype: The quantum data type of the bitsize of the left register.
    """

    dtype: QDType

    @cached_property
    def signature(self) -> Signature:
        return Signature(
            [
                Register('reg', self.dtype, shape=tuple(), side=Side.LEFT),
                Register('reg', QBit(), shape=(self.dtype.num_qubits,), side=Side.RIGHT),
            ]
        )

    def adjoint(self) -> 'Bloq':
        return Join(dtype=self.dtype)

    def as_cirq_op(self, qubit_manager, reg: 'CirqQuregT') -> Tuple[None, Dict[str, 'CirqQuregT']]:
        return None, {'reg': reg.reshape((self.dtype.num_qubits, 1))}

    def _t_complexity_(self) -> 'TComplexity':
        return TComplexity()

    def on_classical_vals(self, reg: int) -> Dict[str, 'ClassicalValT']:
        return {'reg': ints_to_bits(np.array([reg]), self.dtype.num_qubits)[0]}

    def add_my_tensors(
        self,
        tn: qtn.TensorNetwork,
        tag: Any,
        *,
        incoming: Dict[str, 'SoquetT'],
        outgoing: Dict[str, 'SoquetT'],
    ):
        tn.add(
            qtn.Tensor(
                data=np.eye(2**self.dtype.num_qubits, 2**self.dtype.num_qubits).reshape(
                    (2,) * self.dtype.num_qubits + (2**self.dtype.num_qubits,)
                ),
                inds=outgoing['reg'].tolist() + [incoming['reg']],
                tags=['Split', tag],
            )
        )

    def get_ctrl_system(self, ctrl_spec=None) -> Tuple['Bloq', 'AddControlledT']:
        def add_controlled(
            bb: 'BloqBuilder', ctrl_soqs: Sequence['SoquetT'], in_soqs: Dict[str, 'SoquetT']
        ) -> Tuple[Iterable['SoquetT'], Iterable['SoquetT']]:
            # ignore `ctrl_soq` and pass it through for bookkeeping operation.
            out_soqs = bb.add_t(self, **in_soqs)
            return ctrl_soqs, out_soqs

        return self, add_controlled

    def wire_symbol(self, soq: 'Soquet') -> 'WireSymbol':
        if soq.reg.shape:
            text = f'[{", ".join(str(i) for i in soq.idx)}]'
            return directional_text_box(text, side=soq.reg.side)
        return directional_text_box(' ', side=soq.reg.side)


@frozen
class Join(Bloq):
    """Join a length-`n` array-register into one register of bitsize `n`.

    Attributes:
        dtype: The quantum data type of the right register.
    """

    dtype: QDType

    @cached_property
    def signature(self) -> Signature:
        return Signature(
            [
                Register('reg', QBit(), shape=(self.dtype.num_qubits,), side=Side.LEFT),
                Register('reg', self.dtype, shape=tuple(), side=Side.RIGHT),
            ]
        )

    def adjoint(self) -> 'Bloq':
        return Split(dtype=self.dtype)

    def as_cirq_op(self, qubit_manager, reg: 'CirqQuregT') -> Tuple[None, Dict[str, 'CirqQuregT']]:
        return None, {'reg': reg.reshape(self.dtype.num_qubits)}

    def _t_complexity_(self) -> 'TComplexity':
        return TComplexity()

    def add_my_tensors(
        self,
        tn: qtn.TensorNetwork,
        tag: Any,
        *,
        incoming: Dict[str, 'SoquetT'],
        outgoing: Dict[str, 'SoquetT'],
    ):
        tn.add(
            qtn.Tensor(
                data=np.eye(2**self.dtype.num_qubits, 2**self.dtype.num_qubits).reshape(
                    (2,) * self.dtype.num_qubits + (2**self.dtype.num_qubits,)
                ),
                inds=incoming['reg'].tolist() + [outgoing['reg']],
                tags=['Join', tag],
            )
        )

    def on_classical_vals(self, reg: 'NDArray[np.uint8]') -> Dict[str, int]:
        return {'reg': bits_to_ints(reg)[0]}

    def get_ctrl_system(
        self, ctrl_spec: Optional['CtrlSpec'] = None
    ) -> Tuple['Bloq', 'AddControlledT']:
        def add_controlled(
            bb: 'BloqBuilder', ctrl_soqs: Sequence['SoquetT'], in_soqs: Dict[str, 'SoquetT']
        ) -> Tuple[Iterable['SoquetT'], Iterable['SoquetT']]:
            # ignore `ctrl_soq` and pass it through for bookkeeping operation.
            out_soqs = bb.add_t(self, **in_soqs)
            return ctrl_soqs, out_soqs

        return self, add_controlled

    def wire_symbol(self, soq: 'Soquet') -> 'WireSymbol':
        if soq.reg.shape:
            text = f'[{", ".join(str(i) for i in soq.idx)}]'
            return directional_text_box(text, side=soq.reg.side)
        return directional_text_box(' ', side=soq.reg.side)


@frozen
class Partition(Bloq):
    """Partition a generic index into multiple registers.

    Args:
        n: The total bitsize of the un-partitioned register
        regs: Registers to partition into. The `side` attribute is ignored.
        partition: `False` means un-partition instead.

    Registers:
        x: the un-partitioned register. LEFT by default.
        [user spec]: The registers provided by the `regs` argument. RIGHT by default.
    """

    n: int
    regs: Tuple[Register, ...]
    partition: bool = True

    @cached_property
    def signature(self) -> 'Signature':
        lumped = Side.LEFT if self.partition else Side.RIGHT
        partitioned = Side.RIGHT if self.partition else Side.LEFT

        return Signature(
            [Register('x', QAny(bitsize=self.n), side=lumped)]
            + [attrs.evolve(reg, side=partitioned) for reg in self.regs]
        )

    def adjoint(self):
        return attrs.evolve(self, partition=not self.partition)

    def as_cirq_op(self, qubit_manager, **cirq_quregs) -> Tuple[None, Dict[str, 'CirqQuregT']]:
        if self.partition:
            outregs = {}
            start = 0
            for reg in self.regs:
                shape = reg.shape + (reg.bitsize,)
                size = np.prod(shape)
                outregs[reg.name] = np.array(cirq_quregs['x'][start : start + size]).reshape(shape)
                start += size
            return None, outregs
        else:
            return None, {'x': np.concatenate([v.ravel() for _, v in cirq_quregs.items()])}

    def _t_complexity_(self) -> 'TComplexity':
        return TComplexity()

    def add_my_tensors(
        self,
        tn: qtn.TensorNetwork,
        tag: Any,
        *,
        incoming: Dict[str, 'SoquetT'],
        outgoing: Dict[str, 'SoquetT'],
    ):
        unitary_shape = []
        soquets = []
        _incoming = incoming if self.partition else outgoing
        _outgoing = outgoing if self.partition else incoming
        for reg in self.regs:
            for i in range(int(np.prod(reg.shape))):
                unitary_shape.append(2**reg.bitsize)
                if isinstance(_outgoing[reg.name], np.ndarray):
                    soquets.append(_outgoing[reg.name].ravel()[i])
                else:
                    soquets.append(_outgoing[reg.name])

        tn.add(
            qtn.Tensor(
                data=np.eye(2**self.n, 2**self.n).reshape(
                    tuple(unitary_shape) + (2**self.n,)
                ),
                inds=soquets + [_incoming['x']],
                tags=['Partition', tag],
            )
        )

    def _classical_partition(self, x: int) -> Dict[str, 'ClassicalValT']:
        out_vals = {}
        xbits = ints_to_bits(x, self.n)[0]
        start = 0
        for reg in self.regs:
            size = np.prod(reg.shape + (reg.bitsize,))
            bits_reg = xbits[start : start + size]
            if reg.shape == ():
                out_vals[reg.name] = bits_to_ints(bits_reg)[0]
            else:
                ints_reg = bits_to_ints(
                    [
                        bits_reg[i * reg.bitsize : (i + 1) * reg.bitsize]
                        for i in range(np.prod(reg.shape))
                    ]
                )
                out_vals[reg.name] = np.array(ints_reg).reshape(reg.shape)
            start += size
        return out_vals

    def _classical_unpartition(self, **vals: 'ClassicalValT'):
        out_vals = []
        for reg in self.regs:
            if isinstance(vals[reg.name], np.ndarray):
                out_vals.append(ints_to_bits(vals[reg.name].ravel(), reg.bitsize).ravel())
            else:
                out_vals.append(ints_to_bits(vals[reg.name], reg.bitsize)[0])
        big_int = np.concatenate(out_vals)
        return {'x': bits_to_ints(big_int)[0]}

    def on_classical_vals(self, **vals: 'ClassicalValT') -> Dict[str, 'ClassicalValT']:
        if self.partition:
            return self._classical_partition(vals['x'])
        else:
            return self._classical_unpartition(**vals)

    def wire_symbol(self, soq: 'Soquet') -> 'WireSymbol':
        if soq.reg.shape:
            text = f'[{",".join(str(i) for i in soq.idx)}]'
            return directional_text_box(text, side=soq.reg.side)
        return directional_text_box(' ', side=soq.reg.side)


@frozen
class Allocate(Bloq):
    """Allocate an `n` bit register.

    Attributes:
          dtype: the quantum data type of the allocated register.
    """

    dtype: QDType

    @cached_property
    def signature(self) -> Signature:
        return Signature([Register('reg', self.dtype, side=Side.RIGHT)])

    def adjoint(self) -> 'Bloq':
        return Free(self.dtype)

    def on_classical_vals(self) -> Dict[str, int]:
        return {'reg': 0}

    def _t_complexity_(self) -> 'TComplexity':
        return TComplexity()

    def add_my_tensors(
        self,
        tn: 'qtn.TensorNetwork',
        tag: Any,
        *,
        incoming: Dict[str, 'SoquetT'],
        outgoing: Dict[str, 'SoquetT'],
    ):
        data = np.zeros(1 << self.dtype.num_qubits)
        data[0] = 1
        tn.add(qtn.Tensor(data=data, inds=(outgoing['reg'],), tags=['Allocate', tag]))

    def wire_symbol(self, soq: 'Soquet') -> 'WireSymbol':
        assert soq.reg.name == 'reg'
        return directional_text_box('alloc', Side.RIGHT)


@frozen
class Free(Bloq):
    """Free (i.e. de-allocate) an `n` bit register.

    The tensor decomposition assumes the `n` bit register is uncomputed and is in the $|0^{n}>$
    state before getting freed. To verify that is the case, one can compute the resulting state
    vector after freeing qubits and make sure it is normalized.

    Attributes:
        dtype: The quantum data type of the register to be freed.
    """

    dtype: QDType

    @cached_property
    def signature(self) -> Signature:
        return Signature([Register('reg', self.dtype, side=Side.LEFT)])

    def adjoint(self) -> 'Bloq':
        return Allocate(self.dtype)

    def on_classical_vals(self, reg: int) -> Dict[str, 'ClassicalValT']:
        if reg != 0:
            raise ValueError(f"Tried to free a non-zero register: {reg}.")
        return {}

    def _t_complexity_(self) -> 'TComplexity':
        return TComplexity()

    def add_my_tensors(
        self,
        tn: 'qtn.TensorNetwork',
        tag: Any,
        *,
        incoming: Dict[str, 'SoquetT'],
        outgoing: Dict[str, 'SoquetT'],
    ):
        data = np.zeros(1 << self.dtype.num_qubits)
        data[0] = 1
        tn.add(qtn.Tensor(data=data, inds=(incoming['reg'],), tags=['Free', tag]))

    def wire_symbol(self, soq: 'Soquet') -> 'WireSymbol':
        assert soq.reg.name == 'reg'
        return directional_text_box('free', Side.LEFT)


@frozen
class ArbitraryClifford(Bloq):
    """A bloq representing an arbitrary `n`-qubit clifford operation.

    In the surface code architecture, clifford operations are generally considered
    cheaper than non-clifford gates. Each clifford also has roughly the same cost independent
    of what particular operation it is doing.

    You can use this to bloq to represent an arbitrary clifford operation e.g. in bloq_counts
    resource estimates where the details are unimportant for the resource estimation task
    at hand.
    """

    n: Union[int, Expr]

    @cached_property
    def signature(self) -> Signature:
        return Signature([Register('x', QAny(bitsize=self.n))])

    def _t_complexity_(self) -> 'TComplexity':
        return TComplexity(clifford=1)


@frozen
class Cast(Bloq):
    """Cast a register from one n-bit QDType to another QDType.


    Args:
        in_qdtype: Input QDType to cast from.
        out_qdtype: Output QDType to cast to.

    Registers:
        in: input register to cast from.
        out: input register to cast to.
    """

    inp_dtype: QDType
    out_dtype: QDType
    shape: Tuple[int, ...] = attrs.field(
        default=tuple(), converter=lambda v: (v,) if isinstance(v, int) else tuple(v)
    )

    def __attrs_post_init__(self):
        if isinstance(self.inp_dtype.num_qubits, int):
            if self.inp_dtype.num_qubits != self.out_dtype.num_qubits:
                raise ValueError("Casting only permitted between same sized registers.")

    def adjoint(self) -> 'Bloq':
        return Cast(inp_dtype=self.out_dtype, out_dtype=self.inp_dtype)

    @cached_property
    def signature(self) -> Signature:
        return Signature(
            [
                Register('reg', dtype=self.inp_dtype, shape=self.shape, side=Side.LEFT),
                Register('reg', dtype=self.out_dtype, shape=self.shape, side=Side.RIGHT),
            ]
        )

    def add_my_tensors(
        self,
        tn: qtn.TensorNetwork,
        tag: Any,
        *,
        incoming: Dict[str, 'SoquetT'],
        outgoing: Dict[str, 'SoquetT'],
    ):
        tn.add(
            qtn.Tensor(
                data=np.eye(2**self.inp_dtype.num_qubits, 2**self.inp_dtype.num_qubits),
                inds=[outgoing['reg']] + [incoming['reg']],
                tags=['Cast', tag],
            )
        )

    def on_classical_vals(self, reg: int) -> Dict[str, 'ClassicalValT']:
        # TODO: Actually cast the values https://github.com/quantumlib/Qualtran/issues/734
        return {'reg': reg}

    def as_cirq_op(self, qubit_manager, reg: 'CirqQuregT') -> Tuple[None, Dict[str, 'CirqQuregT']]:
        return None, {'reg': reg}

    def _t_complexity_(self) -> 'TComplexity':
        return TComplexity()


@frozen
class Power(GateWithRegisters):
    """Wrapper that repeats the given `bloq` `power` times.

    `Bloq` must have only THRU registers.

    Args:
        bloq: Bloq to repeat
        power: Number of times to repeat the Bloq

    Registers:
        Same as `self.bloq.signature`
    """

    bloq: Bloq
    power: SymbolicInt

    def __attrs_post_init__(self):
        if any(reg.side != Side.THRU for reg in self.bloq.signature):
            raise ValueError('Bloq to repeat must have only THRU registers')
        if self.power < 1:
            raise ValueError(f'{self.power=} must be a positive integer.')

    def adjoint(self) -> 'Bloq':
        return Power(self.bloq.adjoint(), self.power)

    @cached_property
    def signature(self) -> Signature:
        return self.bloq.signature

    def build_composite_bloq(self, bb: 'BloqBuilder', **soqs: 'SoquetT') -> Dict[str, 'SoquetT']:
        for _ in range(self.power):
            soqs = bb.add_d(self.bloq, **soqs)
        return soqs

    def build_call_graph(self, ssa: 'SympySymbolAllocator') -> Set['BloqCountT']:
        return {(self.bloq, self.power)}
