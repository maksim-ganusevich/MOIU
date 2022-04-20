import numpy as np


def k_check(k: np.matrix):
    for j in range(k.shape[0] - 1, -1, -1):
        if k.tolist()[j][0] < 0:
            return j
    return -1


def dual_simplex_method(c: np.matrix, A: np.matrix, b: np.matrix, B: list):
    m, n = A.shape
    B = [i - 1 for i in B]
    while True:
        Ab = A[:, B]
        inverse_ab = np.matrix(Ab.getI())
        cb = c[B, :]
        y = (cb.T * inverse_ab).T
        kb = inverse_ab * b
        k = np.matrix(np.zeros(c.shape[0])).T
        k[B, :] = kb
        jk = k_check(k)
        if jk == -1:
            return k

        k_index = B.index(jk)
        delta_y = inverse_ab[k_index, :].T

        μ = {}
        for j in set(range(n)) - set(B):
            μ[j] = float(delta_y.T * A[:, j])

        σ = {}
        checker_compatibility = False
        for j in set(range(n)) - set(B):
            if μ[j] < 0:
                σ[j] = (float(c[j, 0]) - float(A[:, j].T * y)) \
                       / μ[j]
                checker_compatibility = True

        if not checker_compatibility:
            raise BaseException("task is not compatible")

        j0 = min(σ, key=σ.get)
        B[k_index] = j0
    pass
