OPENQASM 3.0;
include "stdgates.inc";

def oracle(qubit[DEUTSCH_SIZE] q, qubit[1] ancilla, bool IS_CONST) {
    int[16] n = DEUTSCH_SIZE;
    if(IS_CONST && (q[0]&1)){
        x ancilla;
    }
}