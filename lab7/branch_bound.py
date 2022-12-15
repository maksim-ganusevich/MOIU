import math
from copy import deepcopy

import numpy as np
from lab4.dual_simplex import dual_simplex_method


class Task:
    def __init__(self, c, A, b, d, alpha, delta):
        self.c = deepcopy(c)
        self.A = deepcopy(A)
        self.b = deepcopy(b)
        self.d = deepcopy(d)
        self.alpha = deepcopy(alpha)
        self.delta = deepcopy(delta)


def branch_and_bound_method(c_: np.matrix, A_: np.matrix, b_: np.matrix, d_: np.matrix) -> np.matrix:
    n, m = A_.shape
    change = []
    for i in range(c_.shape[0]):
        if c_[i, 0] > 0:
            c_[i, 0] *= -1
            A_[:, i] *= -1
            d_[i, :] *= -1
            d_[i, 0], d_[i, 1] = d_[i, 1], d_[i, 0]
            change.append(i)

    A = np.hstack((np.vstack((A_, np.eye(n))), np.eye(n+m)))
    b = np.vstack((b_, d_[:, 1]))
    d = np.vstack((d_[:, 0], np.matrix(np.zeros((n + m, 1)))))
    c = np.vstack((c_, np.matrix(np.zeros((n + m, 1)))))
    stack = [Task(c, A, b, d, 0, d)]
    x_opt = []
    r = float('-inf')
    it = 0
    while len(stack) > 0:
        cur_task = stack.pop()
        alpha0 = cur_task.alpha + cur_task.c.T * cur_task.d
        b0 = cur_task.b - cur_task.A * cur_task.d
        y = [0] * (m + n)
        B = list(range(n + 1, 2 * n + m + 1))
        x = dual_simplex_method(cur_task.c, cur_task.A,  b0, B)
        checker = True
        x_iter = np.squeeze(np.asarray(x)).tolist()
        if math.floor(float(x_iter * cur_task.c + alpha0)) > r:
            for val in x_iter:
                if abs(round(val) - val) > 10 ** -6:
                    checker = False
                    if len(x_opt) < 1:
                        cur_ind = x_iter.index(val)
                        break

            if not checker:
                if it < 1:
                    cur_ind = 1
                b00 = deepcopy(b0)
                b00[m+cur_ind] = math.floor(x[cur_ind])
                d0 = np.matrix(np.zeros((2*n + m, 1)))
                stack.append(Task(c, A, b00, d0, alpha0, d0 + cur_task.delta))
                d0[cur_ind, 0] = math.ceil(x[cur_ind])
                stack.append(Task(c, A, b0, d0, alpha0, d0 + cur_task.delta))

            else:
                r = math.floor(float(x_iter * cur_task.c + alpha0))
                x_opt = np.squeeze(np.asarray(x + cur_task.delta)).tolist()

        it += 1

    for i in change:
        x_opt[i] *= -1
    return x_opt[:len(c_)], r
