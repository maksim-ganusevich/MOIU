import numpy as np
from copy import deepcopy


def marker(B_marked: dict, index: tuple):
    value = not B_marked[index]
    for i, j in B_marked.keys():
        if index[0] == i:
            if B_marked[(i, j)] is None:
                B_marked[(i, j)] = value
                marker(B_marked, (i, j))
        if index[1] == j:
            if B_marked[(i, j)] is None:
                B_marked[(i, j)] = value
                marker(B_marked, (i, j))


def potential_method(a: list, b: list, c: np.matrix) -> np.matrix:
    if c.shape[1] != len(b) or c.shape[0] != len(b):
        raise AttributeError("wrong attribute sizes")
    if (diff := sum(a) - sum(b)) > 0:
        b.append(diff)
        c = np.append(c, [[0] * c.shape[0]], axis=1)
    elif diff < 0:
        a.append(-diff)
        c = np.append(c, [[0] * c.shape[1]], axis=0)

    x = np.zeros((len(a), len(b)))
    B = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        m = min([a[i], b[j]])
        x[i, j] = m
        B.append((i, j))
        a[i] -= m
        b[j] -= m
        if a[i] == 0 and i < len(a) - 1:
            i += 1
        elif b[j] == 0:
            j += 1

    while True:
        a_vals = []
        b_vals = []
        for i, j in B:
            u_vals = [0] * a.shape[0]
            v_vals = [0] * b.shape[0]
            u_vals[i] = 1
            v_vals[j] = 1
            a_vals.append(u_vals + v_vals)
            b_vals.append(c[i, j])
        u_vals = [0] * (a.shape[0] + b.shape[0])
        u_vals[0] = 1
        a_vals.append(u_vals)
        b_vals.append(0)

        sol = np.linalg.solve(a_vals, b_vals)
        u = sol[:len(a)]
        v = sol[len(b):]

        j0 = None
        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                if (i, j) not in B and u[i] + v[j] > c[i, j]:
                    j0 = (i, j)
                    break
            if j0 is not None:
                break

        if j0 is None:
            return x

        B.append(j0)

        B = sorted(B)
        B_copy = deepcopy(B)

        for i in range(x.shape[0]):
            counter = 0
            for j in range(x.shape[1]):
                if (i, j) in B_copy:
                    counter += 1
            if counter <= 1:
                for j in range(x.shape[1]):
                    if (i, j) in B_copy:
                        B_copy.remove((i, j))

        for j in range(x.shape[1]):
            counter = 0
            for i in range(x.shape[0]):
                if (i, j) in B_copy:
                    counter += 1
            if counter <= 1:
                for i in range(x.shape[0]):
                    if (i, j) in B_copy:
                        B_copy.remove((i, j))

        B_marked = {item: None for item in B_copy}
        B_marked[j0] = True

        marker(B_marked, j0)

        min_minus_x = np.inf
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                if not B_marked.get((i, j), True):
                    min_minus_x = min(min_minus_x, x[i, j])

        for (i, j) in B_marked.keys():
            if B_marked[(i, j)]:
                x[i, j] += min_minus_x
            else:
                x[i, j] -= min_minus_x

        for i, j in B:
            if x[i, j] == 0 and not B_marked.get((i, j), True):
                B.remove((i, j))
                break
