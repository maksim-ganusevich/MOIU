from lab2.main_phase import main_phase
from lab3.first_phase import first_phase
from lab4.dual_simplex import dual_simplex_method
from lab5.potential_method import potential_method
from lab6.quadratic_programming import quadratic_prog
from lab7.branch_bound import branch_and_bound_method
from lab8.clipping_constraint import clipping_constraint
from lab9.max_path import find_max_path
from lab10.profit_maximization import profit_maximization
from lab11.max_flow import start_f_f
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
    print(first_phase(c, A, b))
    """
    """
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
    print(dual_simplex_method(c, A, b, B))
    """

    """
    a = np.array([100, 300, 300], float)
    b = np.array([300, 200, 200], float)
    c = np.array([[8, 4, 1],
                  [8, 4, 3],
                  [9, 7, 5]], float)
    print(potential_method(a, b, c))
    """
    """
    A = np.matrix([[1, 0, 2, 1],
                  [0, 1, -1, 2]])
    c = np.matrix([-8, -6, -4, -6]).T
    x = np.matrix([2., 3., 0., 0.]).T
    J = [1, 2]
    Js = [1, 2]
    H = np.matrix([[2, 1, 1, 0],
                  [1, 1, 0, 0],
                  [1, 0, 1, 0],
                  [0, 0, 0, 0]])
    print(quadratic_prog(A, c, x, J, Js, H))
    """
    """
    c = np.matrix([[1],
                   [1]])
    A = np.matrix([[5, 9],
                   [9, 5]])
    b = np.matrix([[63],
                   [63]])
    d = np.matrix([[1, 6],
                   [1, 6]])
    print(branch_and_bound_method(c, A, b, d))
    """
    """
    print("lab2")
    print(clipping_constraint())
    """
    """
    print("lab3")
    find_max_path()
    """
    """
    print("lab4")
    print(profit_maximization())
    """

    print("lab5")
    start_f_f()



if __name__ == '__main__':
    main()
