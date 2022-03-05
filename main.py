from lab1.recalculation import recalculation
import numpy as np


def main():
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


if __name__ == '__main__':
    main()
