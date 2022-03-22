import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

fig = plt.figure()
ax = fig.subplots()
ax.plot([0, 0.5, 1], [0, 0.5, 1], color='white')
ax.grid()

# Defining the cursor
cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                color='k', linewidth=1)


def bezier(P, i):
    X = i * [0]
    Y = i * [0]
    t = np.linspace(0, 1, i)
    for k in range(i):
        T = t[k]
        X[k] = ((1 - T) ** 3) * P[0, 0] + 3 * T * (1 - T) ** 2 * P[1, 0] + 3 * T ** 2 * (1 - T) * P[2, 0] + T ** 3 * P[
            3, 0]
        Y[k] = (1 - T) ** 3 * P[0, 1] + 3 * T * (1 - T) ** 2 * P[1, 1] + 3 * T ** 2 * (1 - T) * P[2, 1] + T ** 3 * P[
            3, 1]

    return X, Y


def trace_bezier(P, i):
    X, Y = bezier(P, i)
    plt.clf()
    plt.grid()
    plt.plot(P[:, 0], P[:, 1], 'o', color='k')
    plt.plot(P[:, 0], P[:, 1], color='k', alpha=0.5, linestyle='--')
    plt.plot(X, Y)


coor = np.array([[0, 0]])


def onclick(event):
    global coor

    if not event.inaxes:
        return

    coor = np.append(coor, [[event.xdata, event.ydata]], axis=0)
    x = event.xdata
    y = event.ydata
    # printing the values of the selected point
    plt.plot(x, y, 'o', color='k')
    if coor.shape[0] == 4:
        trace_bezier(coor, 50)
        coor = np.delete(coor, (0, 1, 2, 3), axis=0)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    fig.canvas.draw()  # redraw the figure


plt.connect('button_press_event', onclick)

plt.show()

