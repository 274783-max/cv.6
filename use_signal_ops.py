import matplotlip.pyplot as plt

    plt.plot([1, 2, 3], [3, 1, 4])
    plt.show()


def load_signal_from_txt(path):
    with open(path, mode="r") as file:
        content = file.read()
    return list(float(path))

def plot_signal(values)





