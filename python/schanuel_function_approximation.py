def main():
    import matplotlib.pyplot as plt
    import numpy as np
    import random

    a_min = 0.25
    a_max = 0.45

    a = a_min + (a_max - a_min) * random.random()
    domain = np.linspace(0, 10, 11)
    y = a * domain
    y_floor = np.floor(y)
    y_ceil = np.ceil(y)
    y_round = np.round(y)

    figure, axs = plt.subplots(1, 3)

    for ax in axs:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)

        ax.set_xticks(np.linspace(0, 10, 11))
        ax.set_yticks(np.linspace(0, 5, 6))

        for tick in ax.xaxis.get_major_ticks():
            tick.tick1line.set_visible(False)
            tick.tick2line.set_visible(False)
            tick.label1.set_visible(False)
            tick.label2.set_visible(False)

        for tick in ax.yaxis.get_major_ticks():
            tick.tick1line.set_visible(False)
            tick.tick2line.set_visible(False)
            tick.label1.set_visible(False)
            tick.label2.set_visible(False)

        ax.grid(which='major', axis='both')

    rect_floor_coords = []
    rect_ceil_coords = []
    rect_round_coords = []
    for x, (floor_x, ceil_x, round_x) in enumerate(zip(y_floor, y_ceil, y_round)):
        rect_floor_coords.append([x, x + 1, x + 1, x])
        rect_floor_coords.append([floor_x, floor_x, floor_x + 1, floor_x + 1])
        rect_floor_coords.append('b')

        rect_ceil_coords.append([x, x + 1, x + 1, x])
        rect_ceil_coords.append([ceil_x, ceil_x, ceil_x + 1, ceil_x + 1])
        rect_ceil_coords.append('b')

        rect_round_coords.append([x, x + 1, x + 1, x])
        rect_round_coords.append([round_x, round_x, round_x + 1, round_x + 1])
        rect_round_coords.append('b')

    axs[0].plot(y, color='r')
    axs[0].fill(*rect_floor_coords)

    axs[1].plot(y, color='r')
    axs[1].fill(*rect_ceil_coords)

    axs[2].plot(y, color='r')
    axs[2].fill(*rect_round_coords)

    fig = plt.gcf()
    fig.set_size_inches(20, 6)

    plt.show()


if __name__ == '__main__':
    main()
