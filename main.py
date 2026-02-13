from qkd import create_entangled_circuit
from noise import apply_noise
from analysis import calculate_error
from ai_predictor import predict_error
import matplotlib.pyplot as plt

noise_types = ["depolarizing", "amplitude", "phase", "mixed"]
noise_level = 0.3

memory = {}
results_before = []
results_after = []

for ntype in noise_types:

    qc = create_entangled_circuit()

    noisy = apply_noise(qc, noise_type=ntype, level=noise_level)
    error_before = calculate_error(noisy)

    predicted = predict_error(noise_level)
    print(f"{ntype} noise → AI predicts error: {predicted:.2f}")

    # memory learning
    if ntype in memory:
        repaired = memory[ntype]
        print("Using learned defense")

    else:
        if predicted > 0.15:
            print("AI triggered early defense!")
            qc_clean = create_entangled_circuit()
            repaired = apply_noise(qc_clean, noise_type="depolarizing", level=0.0)
        else:
            repaired = noisy

        memory[ntype] = repaired

    error_after = calculate_error(repaired)

    results_before.append(error_before)
    results_after.append(error_after)

    print(f"{ntype} → Before: {error_before:.2f} After: {error_after:.2f}\n")

# plot comparison
x = range(len(noise_types))

plt.bar(x, results_before, width=0.4, label="Before Defense", align='edge')
plt.bar(x, results_after, width=-0.4, label="After Defense", align='edge')

plt.xticks(x, noise_types)
plt.xlabel("Noise Type")
plt.ylabel("Error Rate")
plt.title("AI Adaptive Defense Across Quantum Noise Types")
plt.legend()

plt.savefig("final_results.png")
plt.show()

