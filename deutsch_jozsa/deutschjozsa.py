# Copyright 2025 qBraid
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

"""
Deutsch-Jozsa Algorithm Implementation

"""
import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union

import pyqasm
from pyqasm.modules.base import QasmModule

from qbraid_algorithms.utils import _prep_qasm_file


def generate_program(bitstring: Union[str, list[int]]) -> QasmModule:
    """
    Load the Deutsch-Jozsa circuit as a pyqasm module.

    Args:
        bitstring (Union[str, list[int]]): The hidden bitstring `s` as a string of '0's and '1's

    Returns:
        PyQASM module containing the Deutsch-Jozsa circuit
    """

    # Load the Deutsch-Jozsa QASM files into a staging directory
    temp_dir = tempfile.mkdtemp()
    deutsch_jozsa_src = Path(__file__).parent.parent / "qasm_resources/dj.qasm"
    deutsch_jozsa_dst = os.path.join(temp_dir, "dj.qasm")
    deutsch_jozsa_sub_src = (
        Path(__file__).parent.parent / "qasm_resources/dj_subroutine.qasm"
    )
    deutsch_jozsa_sub_dst = os.path.join(temp_dir, "dj_subroutine.qasm")
    shutil.copy(deutsch_jozsa_src, deutsch_jozsa_dst)
    shutil.copy(deutsch_jozsa_sub_src, deutsch_jozsa_sub_dst)

    # Replace variable placeholders with user-defined parameters
    replacements = _generate_replacements(bitstring)
    _prep_qasm_file(deutsch_jozsa_sub_dst, replacements)
    _prep_qasm_file(deutsch_jozsa_dst, replacements)

    # Load the algorithm as a pyqasm module
    module = pyqasm.load(deutsch_jozsa_dst)

    # Delete the created files
    shutil.rmtree(temp_dir)

    return module


def save_to_qasm(
    bitstring: Union[str, list[int]], quiet: bool = False, path: Optional[str] = None
) -> None:
    """
    Creates a Deutsch-Jozsa subroutine module with user-defined hidden bitstring.

    Args:
        bitstring (Union[str, list[int]]): The hidden bitstring.
        quiet (bool): If True, suppresses output messages.
        path (str): The directory path where the Deutsch-Jozsa subroutine will be created.
                   If None, creates in the current working directory.

    Returns:
        None
    """
    # Copy the B-V subroutine QASM file to the specified or current working directory
    deutsch_jozsa_src = (
        Path(__file__).parent.parent / "qasm_resources/dj_subroutine.qasm"
    )
    if path is None:
        deutsch_jozsa_dst = os.path.join(os.getcwd(), "dj.qasm")
    else:
        deutsch_jozsa_dst = os.path.join(path, "dj.qasm")
    shutil.copy(deutsch_jozsa_src, deutsch_jozsa_dst)

    # Replace variable placeholders with user-defined parameters
    replacements = _generate_replacements(bitstring)
    _prep_qasm_file(deutsch_jozsa_dst, replacements)

    if not quiet:
        print(f"Subroutine 'deutsch_jozsa' has been added to {deutsch_jozsa_dst}")


def generate_oracle(
    bitstring: Union[str, list[int]], quiet: bool = False, path: Optional[str] = None
) -> None:
    """
    Creates a Deutsch-Jozsa oracle encoded with user-defined hidden bitstring.

    Args:
        bitstring (Union[str, list[int]]): The hidden bitstring `s` as a string
                                   of '0's and '1's
        quiet (bool): If True, suppresses output messages.
        path (str): The directory path where the Deutsch-Jozsa oracle will be created.
                   If None, creates in the current working directory.

    Returns:
        None
    """
    # Copy the oracle QASM file to the specified or current working directory
    oracle_src = Path(__file__).parent.parent / "qasm_resources/oracle.qasm"
    if path is None:
        oracle_dst = os.path.join(os.getcwd(), "oracle.qasm")
    else:
        oracle_dst = os.path.join(path, "oracle.qasm")
    shutil.copy(oracle_src, oracle_dst)

    # Replace variable placeholders with user-defined parameters
    replacements = _generate_replacements(bitstring)
    _prep_qasm_file(oracle_dst, replacements)

    if not quiet:
        print(f"Oracle 'oracle' has been added to {oracle_dst}")


def _convert_bitstring_decimal(bitstring: Union[str, list[int]]) -> int:
    """
    Converts a bitstring (str or list of int) to its decimal integer representation.

    Args:
        bitstring (Union[str, list[int]]): The hidden bitstring of '0's and '1's

    Returns:
        int: Decimal integer representation of the bitstring
    """
    if isinstance(bitstring, list):
        bitstring = "".join(str(b) for b in bitstring)
    # Reverse bitstring for correct qubit ordering
    bitstring_reversed = bitstring[::-1]
    return int(bitstring_reversed, 2)


def _generate_replacements(bitstring: Union[str, list[int]]) -> dict[str, str]:
    """
    Generates a dictionary of replacements for QASM variable placeholders.

    Args:
        bitstring (Union[str, list[int]]): The hidden bitstring of '0's and '1's

    Returns:
        dict[str, str]: Dictionary mapping variable names to their string values
    """
    input_size = len(bitstring)
    decimal_value = _convert_bitstring_decimal(bitstring)
    return {"deutsch_jozsa_SIZE": str(input_size), "SECRET_BITSTRING": str(decimal_value)}