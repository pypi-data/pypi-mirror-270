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
from qualtran import Bloq
from qualtran.bloqs.basic_gates import Rz, TGate
from qualtran.bloqs.chemistry.trotter.hubbard.hopping import _hopping_tile, _plaquette
from qualtran.bloqs.util_bloqs import ArbitraryClifford
from qualtran.resource_counting.generalizers import PHI


def test_hopping_tile(bloq_autotester):
    bloq_autotester(_hopping_tile)


def test_hopping_plaquette(bloq_autotester):
    bloq_autotester(_plaquette)


def catch_rotations(bloq) -> Bloq:
    if isinstance(bloq, Rz):
        if abs(bloq.angle) < 1e-12:
            return ArbitraryClifford(1)
        else:
            return Rz(angle=PHI)
    return bloq


def test_hopping_tile_t_counts():
    bloq = _hopping_tile()
    _, counts = bloq.call_graph(generalizer=catch_rotations)
    assert counts[TGate()] == 8 * bloq.length**2 // 2
    assert counts[Rz(PHI)] == 2 * bloq.length**2 // 2
