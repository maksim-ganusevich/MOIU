import numpy as np


def DynamicProgrammingMethod(V, M):
    n = len(V)
    OPT = [0]
    x = []

    for j in range(1, n):
        v = V[j]
        max_path, max_v = 0, -1  # max по длине ребро и вершина-начало

        for i in range(n):
            if M[i][v] > 0:
                path_len = OPT[V.index(i)] + M[i][v]

                if path_len > max_path:
                    max_path = path_len
                    max_v = i

        OPT.append(max_path)
        x.append(max_v)

    x.append(v)
    x = [i + 1 for i in x]

    return x, max_path


def TopologicalSort(M, s=1):
    n = len(M)

    V_colors = np.zeros(n)
    V_sorted = []
    S = [s - 1]

    while not all(vertex == 2 for vertex in V_colors):
        last_S = S[-1]

        if V_colors[last_S] == 0:
            V_colors[last_S] = 1

            for i in range(n):
                if (M[last_S][i] != 0) and (i not in V_sorted) and (V_colors[i] == 0):
                    S.append(i)

        elif V_colors[last_S] == 1:
            V_colors[last_S] = 2
            while last_S in S:
                S.remove(last_S)
            V_sorted.append(last_S)

    V_sorted.reverse()

    return V_sorted


def find_max_path():
    M = np.array(np.mat(''' 0, 5, 0, 0, 0, 3 ;
                        0, 0, 3, 0, 0, 1 ;
                        0, 0, 0, 1, 0, 0 ;
                        0, 0, 0, 0, 0, 0 ;
                        0, 0, 2, 1, 0, 0 ;
                        0, 0, 0, 0, 4, 0 '''))
    print(M)

    V = TopologicalSort(M)
    print('V: {}\n'.format(V))

    max_path_v, max_path_len = DynamicProgrammingMethod(V, M)

    print(max_path_v, max_path_len)


if __name__ == '__main__':
    find_max_path()
