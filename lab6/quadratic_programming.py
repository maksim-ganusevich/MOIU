import numpy as np


def delta_check(delta: np.matrix) -> int:
    for j in range(delta.shape[0]):
        if delta.tolist()[j][0] < 0:
            return j
    return -1


def quadratic_prog(A: np.matrix, c: np.matrix, x: np.matrix, J: list, Js: list, D: np.matrix) -> np.matrix:
    J = [i - 1 for i in J]
    Js = [i - 1 for i in Js]
    while True:

        A_B = A[:, J]
        c_x = c + D * x
        c_B = c_x[J, :]
        u_x = (-c_B.T * A_B.I).T
        delta_x = (u_x.T * A + c_x.T).T

        j_0 = delta_check(delta_x)
        # step 5
        if j_0 == -1:
            return x
        l = np.matrix(np.zeros(x.shape[0])).T
        l[j_0, 0] = 1

        Ds = (D[Js, :])[:, Js]
        A_Bs = A[:, Js]

        H = np.matrix(np.zeros((Ds.shape[0] + A_Bs.shape[0], Ds.shape[1] + A_Bs.shape[0])))
        H[:Ds.shape[0], :Ds.shape[1]] = Ds[:, :]
        H[: A_Bs.shape[1], Ds.shape[1]:] = A_Bs.T
        H[Ds.shape[0]:, : A_Bs.shape[1]] = A_Bs

        bs = np.matrix(np.zeros(len(Js) + A.shape[0])).T
        bs[:len(Js), :] = D[Js, j_0]
        bs[len(Js):, :] = A[:, j_0]

        x_temp = -1 * H.I * bs

        index = 0
        for i in range(l.shape[0]):
            if i in Js:
                l[i, 0] = x_temp[index]
                index += 1

        tettas = [float("inf")] *  x.shape[0]
        sigma = float(l.T * D * l)
        if sigma > 0:
            tettas[j_0] = abs(delta_x[j_0]) / sigma
        for i in Js:
            if l[i] < 0:
                tettas[i] = -x[i] / l[i]

        tetta0 = float(min(tettas))
        if min(tettas) == float("inf"):
            raise ValueError('The function is not bounded on the set of admissible plans')
        js = tettas.index(tetta0)
        x += tetta0 * l

        if js == j_0:
            Js.append(js)
        elif js in Js and js not in J:
            Js.remove(js)
        elif js in J:
            check = True
            for j_plus in Js:
                if j_plus not in J:
                    if (A_B.T * A[:, j_plus])[J.index(js)] != 0:
                        Js[Js.index(js)] = j_plus
                        J.remove(js)
                        check = False
            if check:
                J[J.index(js)] = j_0
                Js[Js.index((js))] = j_0
