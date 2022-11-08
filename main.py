import numpy as np
import matplotlib.pyplot as plt
from input import (
    R1,
    R2,
    DELTA_T,
    RO,
    C_RO,
    LAMBDA,
    N,
    M,
    A1,
    A2,
    T1,
    T2,
    T0,
)


def create_input():
    dr = (R2 - R1) / N
    dt = DELTA_T / M

    al1 = A1 / LAMBDA
    al2 = A2 / LAMBDA

    r_i = np.linspace(R1, R2, N)

    a__2 = LAMBDA / (C_RO * RO)

    Ai = -1 - (dt * a__2) / (r_i * dr) - (2 * dt * a__2) / (dr**2)
    Bi = (dt * a__2) / (r_i * dr) + (dt * a__2) / (dr**2)
    C = (dt * a__2) / (dr**2)

    return N, M, T0, Ai, Bi, C, al1, al2, dr


def solve(N, M, T0, Ai, Bi, C, al1, al2, dr):
    Alpha = np.empty((N,))
    Beta = np.empty((N,))

    T = np.empty((N, M))
    T[:, 0] = T0

    for j in range(M-1):

        Alpha[0] = 1.0 / (1.0 + al1 * dr)
        Beta[0] = al1 * dr * T1 / (1.0 + al1 * dr)

        for i in range(1, N):
            Alpha[i] = -Bi[i] / (Ai[i] + C * Alpha[i - 1])
            Beta[i] = -(T[i, j] + C * Beta[i - 1]) / (Ai[i] + C * Alpha[i - 1])

        T[N - 1, j + 1] = (T2 * al2 * dr + T[N - 2, j]) / (1.0 +  al2 * dr)

        for i in range(N - 2, -1, -1):
            T[i, j + 1] = Alpha[i] * T[i + 1, j + 1] + Beta[i]

    return T


if __name__ == "__main__":
    import warnings
    warnings.simplefilter("ignore", UserWarning)

    args = create_input()

    T = solve(*args)
    h, w = T.shape

    fig, ax = plt.subplots()

    im = ax.imshow(T, vmin=T.min(), vmax=T.max(), aspect=w/h)

    ax.set_xlabel('T, seconds')
    ax.set_ylabel('R, meters')

    # plot the colorbar
    cbar = fig.colorbar(im)
    cbar.set_label('Temperature, K')
    
    xlables = ax.get_xticklabels()
    ylables = ax.get_yticklabels()

    fmt = lambda x: "{:.3f}".format(x)
    for e in xlables:
        e._x = DELTA_T * e._x / M
        e._text = fmt(e._x)

    for e in ylables:
        e._y = R2 * e._y / N + R1
        e._text = fmt(e._y)

    ax.set_xticklabels(xlables)
    ax.set_yticklabels(ylables)

    # print(np.linspace(R1, R2, 10))

    np.savetxt('out.txt', T[:,-1])
    fig.savefig('plot.png', dpi=fig.dpi)
