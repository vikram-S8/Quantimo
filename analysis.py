def calculate_error(counts):

    total = sum(counts.values())
    error = 0

    for state, value in counts.items():
        if state in ["01", "10"]:
            error += value

    return error / total


