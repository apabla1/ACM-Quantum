OPENQASM 3.0;
include "dj_subroutine.qasm";

qubit[DEUTSCH_SIZE] q;
qubit[1] ancilla;
bit[DEUTSCH_SIZE] b;

bernvaz(q, ancilla);
b = measure q;