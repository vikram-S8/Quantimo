import streamlit as st
import matplotlib.pyplot as plt
import random
import time

from qkd import create_entangled_circuit
from noise import apply_noise
from analysis import calculate_error
from ai_predictor import predict_error, confidence_score, choose_strategy

st.set_page_config(layout="wide")

st.title("🔗Quantum Cybersecurity Research Simulator")

# ======================
# Scenario mode
# ======================

st.sidebar.title("🌐 Quantum Internet Scenario")

scenario = st.sidebar.selectbox(
    "Environment",
    ["Fiber Optic", "Satellite Link", "Deep Space"]
)

scenario_noise = {
    "Fiber Optic": 0.1,
    "Satellite Link": 0.25,
    "Deep Space": 0.4
}

base_noise = scenario_noise[scenario]

st.sidebar.write(f"Base noise level: {base_noise}")

# ======================
# Eve attack toggle
# ======================

eve_mode = st.sidebar.toggle("🕵 Simulate Hacker Eve")

# ======================
# Manual simulation
# ======================

st.header("Single Simulation")

noise_type = st.selectbox(
    "Noise Type",
    ["depolarizing", "amplitude", "phase", "mixed"]
)

noise_level = st.slider("Extra Noise", 0.0, 0.3, 0.1, 0.05)

run = st.button("Run Simulation")

if run:

    total_noise = base_noise + noise_level

    qc = create_entangled_circuit()

    noisy = apply_noise(qc, noise_type, total_noise)
    error_before = calculate_error(noisy)

    # Eve interception
    detection_prob = 0
    if eve_mode:
        eve_spike = random.uniform(0.05, 0.15)
        error_before += eve_spike
        detection_prob = min(1.0, error_before * 1.5)

    predicted = predict_error(total_noise)
    conf = confidence_score(predicted)
    strategy = choose_strategy(predicted)

    st.write(f"AI Confidence: {conf}%")
    st.write(f"Defense Strategy: **{strategy}**")

    if eve_mode:
        st.warning(f"Eavesdropper detected! Detection probability: {detection_prob:.2f}")

    if predicted > 0.15:
        st.error("🚨 DEFENSE ACTIVATED")
        qc_clean = create_entangled_circuit()
        repaired = apply_noise(qc_clean, "depolarizing", 0.0)
    else:
        repaired = noisy

    error_after = calculate_error(repaired)

    st.write(f"Error Before: {error_before:.3f}")
    st.write(f"Error After: {error_after:.3f}")

    fig, ax = plt.subplots()
    ax.bar(["Before", "After"], [error_before, error_after])
    ax.set_ylabel("Error Rate")
    ax.set_title("Defense Result")

    st.pyplot(fig)

# ======================
# Multi-round learning
# ======================

st.header("🧬 Multi-Round Learning Simulation")

if st.button("Run Learning Evolution"):

    errors = []
    noise = base_noise

    for round in range(5):

        qc = create_entangled_circuit()
        noisy = apply_noise(qc, noise_type, noise)

        error = calculate_error(noisy)

        # simulate improvement
        error *= (1 - round * 0.2)

        errors.append(error)
        noise += 0.05
        time.sleep(0.5)

    fig, ax = plt.subplots()
    ax.plot(range(1, 6), errors, marker="o")
    ax.set_xlabel("Round")
    ax.set_ylabel("Error Rate")
    ax.set_title("AI Learning Evolution")

    st.pyplot(fig)


