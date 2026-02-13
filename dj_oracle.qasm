OPENQASM 3.0;
include "stdgates.inc";

def oracle(qubit[DEUTSCH_SIZE] q, qubit[1] ancilla, bool const_value) {
    if (const_value) {
        x ancilla[0];
    } else {
        cx q[0], ancilla[0];
    }
}