import numpy as np
from lab1.recalculation import recalculation


def delta_check(delta: np.matrix):
    for j in range(delta.shape[1]):
        if delta.tolist()[0][j] < 0:
            return j
    return -1


def main_phase(c: np.matrix, a: np.matrix, x: np.matrix, b: np.matrix):
    b = b-1
    Ab = a[:, np.squeeze(b.tolist())]
    inverse_ab = np.matrix(Ab.A)

    cb = np.matrix([float(c[i][0]) for i in np.squeeze(b.tolist())]).T

    while True:
        u = cb.T * inverse_ab
        delta = u * a - c.T
        j = delta_check(delta)
        if j == -1:
            return x, b

        z = inverse_ab * a[:, j]
        sigma = [x[0, b[i, 0]] / z[i, 0] if z[i, 0] > 0 else float("inf") for i in range(z.shape[0])]
        sigma_lst = list(enumerate(sigma, 0))
        sigma_min = min(sigma_lst, key=lambda i: i[1])
        if sigma_min[1] == float("inf"):
            return np.matrix([float("inf") for _ in range(x.shape[1])]), b

        x[0, j] = sigma_min[1]
        for i in range(b.shape[0]):
            x[0, b[i, 0]] -= sigma_min[1] * z[i, 0]

        b[sigma_min[0], 0] = j
        cb = np.matrix([float(c[i][0]) for i in np.squeeze(b.tolist())]).T
        Ab[:, sigma_min[0]] = a[:, j]

        inverse_ab = recalculation(inverse_ab, a[:, j], sigma_min[0] + 1)
        if isinstance(inverse_ab, str):
            return x, b
    pass
