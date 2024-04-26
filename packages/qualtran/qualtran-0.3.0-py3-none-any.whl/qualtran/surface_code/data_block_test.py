#  Copyright 2024 Google LLC
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


import pytest

from qualtran.surface_code import FastDataBlock


@pytest.mark.parametrize(
    ["logical_qubits", "logical_qubits_with_routing"], [[100, 230], [1318, 2740], [12581, 25481]]
)
def test_fast_block(logical_qubits, logical_qubits_with_routing):
    assert FastDataBlock.grid_size(n_algo_qubits=logical_qubits) == logical_qubits_with_routing
