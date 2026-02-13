from sklearn.linear_model import LinearRegression
import numpy as np

noise_data = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5]])
error_data = np.array([0.0, 0.08, 0.18, 0.26, 0.34, 0.42])

model = LinearRegression()
model.fit(noise_data, error_data)

def predict_error(noise_level):
    prediction = model.predict(np.array([[noise_level]]))
    return prediction[0]

def confidence_score(predicted):
    # fake confidence model for demo realism
    conf = min(100, int(predicted * 200 + 50))
    return conf

def choose_strategy(predicted):

    if predicted < 0.10:
        return "No action needed"

    elif predicted < 0.25:
        return "Redundancy injection"

    elif predicted < 0.40:
        return "Entanglement purification"

    else:
        return "Full channel rebuild"

