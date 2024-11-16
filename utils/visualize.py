import matplotlib.pyplot as plt

def plot_predictions(predictions, labels):
    plt.bar(labels, predictions)
    plt.xlabel("Activities")
    plt.ylabel("Confidence")
    plt.show()
