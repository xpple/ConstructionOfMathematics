def main():
    import matplotlib.pyplot as plt
    import numpy as np

    domain = range(10)
    sqrt_2_sequence = np.array([2])
    for n in domain:
        sqrt_2_sequence = np.append(sqrt_2_sequence, sqrt_2_sequence[n] / 2 + 1 / sqrt_2_sequence[n])

    ax = plt.gca()
    ax.set_xticks(np.linspace(0, 10, 11))

    plt.plot(sqrt_2_sequence)

    plt.show()


if __name__ == '__main__':
    main()
