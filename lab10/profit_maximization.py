from copy import deepcopy as dc
import numpy as np


def get_OPT(n, Q, A) -> tuple:
    opt = [dc(A[0])]
    x = [[i for i in range(Q+1)]]
    for k in range(1, n):
        opt.append([])
        x.append([])
        for q in range(Q+1):
            cur_max, cur_x = - np.inf, None
            for xk in range(0, q+1):
                if cur_max < opt[k-1][q-xk] + A[k][xk]:
                    cur_x = xk
                cur_max = max(cur_max, opt[k-1][q-xk] + A[k][xk])
            opt[-1].append(cur_max)
            x[-1].append(cur_x)
    return opt, x


def get_x_values(n, Q, x) -> list:
    answer, x_sum = [x[-1][-1]], x[-1][-1]
    for k in range(n-2, -1, -1):
        answer.append(x[k][Q-x_sum])
        x_sum += answer[-1]
    return answer[::-1]


def profit_maximization():
    A = [[2, 3, 3, 5],
         [1, 0, 2, 1],
         [0, 0, 1, 1]]
    n, Q = len(A), len(A[0]) - 1
    OPT, x = get_OPT(n, Q, A)
    return get_x_values(n, Q, x)


if __name__ == '__main__':
    profit_maximization()
