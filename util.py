from qiskit import QuantumCircuit
from numpy import allclose
from qiskit.quantum_info import Statevector
import random
from numpy import allclose, pi

def check_entangled(qc):
    """Check if qc creates a Bell state from |00>."""
    bell = QuantumCircuit(2)
    bell.h(0)
    bell.cx(0, 1)
    ideal = Statevector.from_label('00').evolve(bell)
    actual = Statevector.from_label('00').evolve(qc)
    if allclose(ideal.data, actual.data, atol=1e-2):
        print("Great job! Your circuit correctly prepares a Bell state.")
    else:
        print("Hmmm, that doesnt look like a correct Bell state. Try again!")
        print("Hint: Did you apply a Hadamard gate to qubit 0 and a CNOT from qubit 0 to 1?")


def check_alice_output(alice_output_func):
    for x in [0, 1]:
        # Create actual circuit
        qc_actual = QuantumCircuit(2)
        qc_actual.h(0)
        qc_actual.cx(0, 1)
        alice_output_func(qc_actual, x)

        # Create expected circuit
        qc_expected = QuantumCircuit(2)
        qc_expected.h(0)
        qc_expected.cx(0, 1)
        if x == 0:
            qc_expected.ry(0, 0)
        else:
            qc_expected.ry(pi / 2, 0)

        # Compare final statevectors
        actual = Statevector.from_label('00').evolve(qc_actual)
        expected = Statevector.from_label('00').evolve(qc_expected)

        if not allclose(actual.data, expected.data, atol=1e-2):
            print(f"Alice's function gives incorrect output for x = {x}")
            return False

    print("Alice's function gives correct output for x = 0 and x = 1")
    return True

def check_bob_output(bob_output_func):
    for y in [0, 1]:
        qc_actual = QuantumCircuit(2)
        qc_actual.h(0)
        qc_actual.cx(0, 1)
        bob_output_func(qc_actual, y)

        qc_expected = QuantumCircuit(2)
        qc_expected.h(0)
        qc_expected.cx(0, 1)
        if y == 0:
            qc_expected.ry(pi / 4, 1)
        else:
            qc_expected.ry(-pi / 4, 1)

        actual = Statevector.from_label('00').evolve(qc_actual)
        expected = Statevector.from_label('00').evolve(qc_expected)

        if not allclose(actual.data, expected.data, atol=1e-2):
            print(f"Bob's function gives incorrect output for y = {y}")
            return False

    print("Bob's function gives correct output for y = 0 and y = 1")
    return True


