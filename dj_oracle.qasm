OPENQASM 3.0;
include "stdgates.inc";

def oracle(qubit[DEUTSCH_SIZE] q, qubit[1] ancilla, bool IS_CONST) {
    if (IS_CONST) {
        x ancilla[0];
    } else {
        cx q[0], ancilla[0];
    }
}