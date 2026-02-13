from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

def create_entangled_circuit():

    qc = QuantumCircuit(2,2)
    qc.h(0)
    qc.cx(0,1)
    qc.measure([0,1],[0,1])

    return qc

