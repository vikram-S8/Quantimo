import matplotlib.pyplot as plt

def plot(error_before, error_after):
    labels = ["Before Defense", "After Defense"]
    values = [error_before, error_after]

    plt.bar(labels, values)
    plt.ylabel("Error Rate")
    plt.title("Quantum Channel Health")
    plt.show()
