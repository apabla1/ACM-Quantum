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


def generate_program(input_size: int, is_const: bool) -> QasmModule:
    """
    Load the Deutsch-Jozsa circuit as a pyqasm module.

    Args:

    Returns:
        PyQASM module containing the Deutsch-Jozsa circuit
    """

    # Load the Deutsch-Jozsa QASM files into a staging directory
    temp_dir = tempfile.mkdtemp()

    base = Path(__file__).parent.parent / "qasm_resources"
    
    dj_src = base / "dj.qasm"
    dj_sub_src = base / "dj_subroutine.qasm"
    dj_oracle_src = base / "dj_oracle.qasm"

    dj_dst = os.path.join(temp_dir, "dj.qasm")
    dj_sub_dst = os.path.join(temp_dir, "dj_subroutine.qasm")
    dj_oracle_dst = os.path.join(temp_dir, "dj_oracle.qasm")

    shutil.copy(dj_src, dj_dst)
    shutil.copy(dj_sub_src, dj_sub_dst)
    shutil.copy(dj_oracle_src, dj_oracle_dst)

    # Replace placeholders
    replacements = _generate_replacements(input_size=input_size, is_const=is_const)
    _prep_qasm_file(dj_oracle_dst, replacements)
    _prep_qasm_file(dj_sub_dst, replacements)
    _prep_qasm_file(dj_dst, replacements)

    return pyqasm.load(dj_dst)


def save_to_qasm(
    input_size: int, is_const: bool, quiet: bool = False, path: Optional[str] = None
) -> None:
    """
    Creates a Deutsch-Jozsa subroutine module.

    Args:
        input_size: Number of input qubits (n).
        is_const: If True, constant oracle; else balanced oracle.
        quiet (bool): If True, suppresses output messages.
        path (str): The directory path where the Deutsch-Jozsa subroutine will be created.
                   If None, creates in the current working directory.

    Returns:
        None
    """
    # Copy the DJ subroutine QASM file to the specified or current working directory
    deutsch_jozsa_src = (
        Path(__file__).parent.parent / "qasm_resources/dj_subroutine.qasm"
    )
    if path is None:
        deutsch_jozsa_dst = os.path.join(os.getcwd(), "dj.qasm")
    else:
        deutsch_jozsa_dst = os.path.join(path, "dj.qasm")
    shutil.copy(deutsch_jozsa_src, deutsch_jozsa_dst)

    # Replace variable placeholders with user-defined parameters
    replacements = _generate_replacements(input_size, is_const)
    _prep_qasm_file(deutsch_jozsa_dst, replacements)

    if not quiet:
        print(f"Subroutine 'deutsch_jozsa' has been added to {deutsch_jozsa_dst}")


def generate_oracle(
    input_size: int, is_const: bool, quiet: bool = False, path: Optional[str] = None
) -> None:
    """
    Creates a Deutsch-Jozsa oracle.

    Args:
        input_size: Number of input qubits (n).
        is_const: If True, constant oracle; else balanced oracle.
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
    replacements = _generate_replacements(input_size, is_const)
    _prep_qasm_file(oracle_dst, replacements)

    if not quiet:
        print(f"Oracle 'oracle' has been added to {oracle_dst}")

def _generate_replacements(input_size: int, is_const: bool) -> dict[str, str]:
    """
    Generates a dictionary of replacements for QASM variable placeholders.

    Args:
        bitstring (Union[str, list[int]]): The hidden bitstring of '0's and '1's

    Returns:
        dict[str, str]: Dictionary mapping variable names to their string values
    """
    return {"DEUTSCH_ZISA": str(input_size), "IS_CONST": "true" if is_const else "false")}