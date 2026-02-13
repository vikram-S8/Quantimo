from qiskit_aer.noise import NoiseModel
from qiskit_aer.noise.errors import (
    depolarizing_error,
    amplitude_damping_error,
    phase_damping_error
)
from qiskit_aer import AerSimulator
from qiskit import transpile


def apply_noise(qc, noise_type="depolarizing", level=0.3, shots=500):

    noise_model = NoiseModel()

    if noise_type == "depolarizing":
        error1 = depolarizing_error(level, 1)
        error2 = depolarizing_error(level, 2)

    elif noise_type == "amplitude":
        error1 = amplitude_damping_error(level)
        error2 = amplitude_damping_error(level).tensor(
            amplitude_damping_error(level)
        )

    elif noise_type == "phase":
        error1 = phase_damping_error(level)
        error2 = phase_damping_error(level).tensor(
            phase_damping_error(level)
        )

    elif noise_type == "mixed":
        error1 = depolarizing_error(level, 1).compose(
            amplitude_damping_error(level)
        )
        error2 = depolarizing_error(level, 2)

    noise_model.add_all_qubit_quantum_error(error1, ['h', 'measure'])
    noise_model.add_all_qubit_quantum_error(error2, ['cx'])

    sim = AerSimulator(noise_model=noise_model)

    compiled = transpile(qc, sim)
    result = sim.run(compiled, shots=shots).result()

    return result.get_counts()
