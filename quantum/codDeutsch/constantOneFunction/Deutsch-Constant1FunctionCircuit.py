from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.reset(qreg_q[0])
circuit.reset(qreg_q[1])
circuit.x(qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.id(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[0])
circuit.id(qreg_q[0])
circuit.id(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])