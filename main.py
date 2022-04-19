from lab2.main_phase import main_phase
from lab3.first_phase import first_phase
from lab4.dual_simplex import dual_simplex_method
import numpy as np


def main():
    """
    m_sqr_mx = np.matrix([[1, 2, 4],
                          [4, 5, 4],
                          [7, 8, 5]])
    m_sqr_mx2 = np.matrix([[1, 2, 2],
                           [4, 5, 5],
                           [7, 8, 9]])
    t = recalculation((m_sqr_mx.getI()).round(14), np.matrix([2, 5, 9]).T, 3)
    print(m_sqr_mx2.getI())
    print(t)
    print((m_sqr_mx2 * t).round(8))
    """
    """
    B = np.matrix([3, 4, 5]).T
    x = np.matrix([0, 0, 1, 3, 2])
    c = np.matrix([1, 1, 0, 0, 0]).T
    A = np.matrix(
        [[-1, 1, 1, 0, 0],
         [1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1]])
    t = main_phase(c, A, x, B)
    print(t)
    """
    """
    A = np.matrix(
        [[1, 1, 1],
         [2, 2, 2]]
    )
    b = np.matrix(
        [[0],
         [0]]
    )
    c = np.matrix(
        [1, 0, 0]
    ).T
    print(first_phase(c, A, b))"""
    c = np.matrix([-4, -3, -7, 0, 0]).T
    A = np.matrix(
        [[-2, -1, -4, 1, 0],
         [-2, -2, -2, 0, 1]]
    )
    b = np.matrix(
        [[-1],
         [-3/2]]
    )
    B = [4, 5]
    dual_simplex_method(c, A, b, B)

    pass


if __name__ == '__main__':
    main()
