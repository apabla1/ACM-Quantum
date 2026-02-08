OPENQASM 3.0;
include "stdgates.inc";
include "dj_oracle.qasm";

def bernvaz(qubit[DEUTSCH_SIZE] q, qubit[1] ancilla, bool IS_CONST) {
    int[16] n = DEUTSCH_SIZE;
    for int i in [0:n - 1] {
        h q[i];
    }
    x ancilla[0];
    h ancilla[0];
    
    oracle(q, ancilla, IS_CONST)

    for int i in [0:n - 1] {
        h q[i];
    }

}