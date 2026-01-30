
"""
Deutsch-Jozsa Algorithm
Deutsch-Jozsa Algorithm

.. admonition:: Deutsch-Jozsa
   :class: note-enhanced

    This module provides a complete implementation of the Deutsch-Jozsa algorithm,
    one of the earliest quantum algorithms demonstrating an exponential separation
    between quantum and classical query complexity.
    The algorithm determines whether a Boolean oracle function is constant or balanced
    using a single quantum query, whereas any deterministic classical algorithm
    requires exponentially many queries in the worst case.

.. admonition:: FORMULATION
   :class: seealso

    Let :math:`f : \\{0,1\\}^n \rightarrow \\{0,1\\}` be a Boolean function promised to be
    either constant or balanced.

    1. **State Preparation**: Initialize :math:`n` input qubits and one ancilla qubit:

        :math:`H^{\\otimes n}|0\\rangle^{\\otimes n} \\otimes H|1\\rangle =
        \\frac{1}{\\sqrt{2^n}} \\sum_{x=0}^{2^n-1} |x\\rangle \\otimes |-\\rangle`

    2. **Oracle Application**: Apply the oracle :math:`U_f` using phase kickback:

        :math:`U_f|x\\rangle|-\\rangle = (-1)^{f(x)}|x\\rangle|-\\rangle`

    3. **Hadamard Transform**: Apply :math:`H^{\\otimes n}` to the input register:

        :math:`H^{\\otimes n}
        \\left[\\frac{1}{\\sqrt{2^n}} \\sum_x (-1)^{f(x)}|x\\rangle\\right]`

    - If :math:`f` is **constant**, the final state is :math:`|0\\rangle^{\\otimes n}`
    - If :math:`f` is **balanced**, the final state is any other computational basis state 

    Measuring the input register distinguishes these cases with certainty,
    demonstrating quantum interference and global phase coherence.

.. admonition:: Functions
   :class: seealso

    .. autosummary::
        :toctree: ../stubs/

        generate_program
        save_to_qasm
        generate_oracle
"""
from .deutschjozsa import generate_program, save_to_qasm, generate_oracle
__all__ = ["generate_program", "save_to_qasm", "generate_oracle"]