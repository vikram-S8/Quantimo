# Quantimo
QUANTIMO- An Quantum Immune System 
⚛️ Intelligent Quantum Intrusion Detection System

An AI-assisted, noise-aware intrusion detection framework for Quantum Key Distribution (QKD) systems.

This project simulates quantum communication under realistic noisy conditions and detects potential eavesdropping using Quantum Bit Error Rate (QBER) analysis and predictive modeling.

📌 Problem Statement

Quantum communication channels are affected by natural noise, making it difficult to distinguish environmental disturbances from malicious interception.

This project builds an adaptive system that differentiates noise from intrusion in QKD environments.

🚀 Key Features

QKD entanglement simulation

Multi-noise channel modeling (depolarizing, amplitude, phase, mixed)

QBER (Quantum Bit Error Rate) measurement

AI-based QBER prediction using regression

Intrusion classification (Safe / Warning / Compromised)

Adaptive defense strategy selection

Secure key fraction estimation

Real-time monitoring dashboard (Streamlit)

Scenario-based simulations (fiber, satellite, deep space)

🧠 How It Works

Generate entangled qubits (QKD setup)

Transmit through a noisy quantum channel

Measure QBER from output states

Predict expected QBER using AI model

Compare measured vs predicted behavior

Classify channel status

Trigger adaptive defense if needed

🛠 Tech Stack

Python

Qiskit

Qiskit Aer (Noise Modeling)

Scikit-learn (AI Prediction)

Streamlit (Dashboard UI)

Matplotlib (Visualization)

NumPy

📂 Project Structure
.
├── qkd.py              # Entanglement generation
├── noise.py            # Noise models
├── analysis.py         # QBER calculation
├── ai_predictor.py     # AI prediction & classification
├── main.py             # Console execution
├── app.py              # Streamlit dashboard
└── README.md

⚙️ Installation
1️⃣ Clone Repository
git clone <your-repo-link>
cd <repo-folder>

2️⃣ Install Dependencies
pip install qiskit qiskit-aer streamlit matplotlib scikit-learn numpy

▶️ Running the Project
Console Mode
python main.py

Dashboard Mode
streamlit run app.py


Open the local URL shown in the terminal.

📊 Example Output

Measured QBER

Predicted QBER

Channel Classification

Secure Key Fraction

Adaptive Defense Strategy

🔐 Why This Matters

Traditional QKD systems abort communication when error rates exceed a threshold.
This system goes further by:

Distinguishing natural noise from malicious intrusion

Predicting channel behavior

Triggering intelligent defense strategies

It bridges classical AI analytics with emerging quantum communication systems.

🏗 Current Status

This project is implemented as a high-fidelity simulation using realistic quantum noise models.

It is designed to be hardware-agnostic and compatible with future quantum communication networks.

📈 Future Scope

Multi-qubit system scaling

Advanced ML intrusion classification

Real-time hardware integration

Edge deployment on HPC infrastructure

Enhanced secure key optimization

👩‍💻 Author

Rania R
Vikram S

📜 License

This project is for academic and research purposes.
