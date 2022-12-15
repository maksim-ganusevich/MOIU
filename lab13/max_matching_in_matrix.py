from Lab6 import bipartite_max_matching
import numpy as np

UPPER_VERTEX = 'v'
LOWER_VERTEX = 'u'


def dfs(visited: set, graph: dict, node: str) -> set:
    visited.add(node)

    if node not in graph.keys():
        return visited

    for adjacent in (x for x in graph[node] if x not in visited):
        return dfs(visited, graph, adjacent)

    return visited


def dual_based_proc(c: np.ndarray):
    n = c.shape[0]
    alphas = [0 for i in range(n)]
    betas = [min(c[:, i]) for i in range(n)]
    while True:
        J_equal = [(i, j) for i, alpha in enumerate(alphas) for j, beta in enumerate(betas) if alpha + beta == c[i, j]]
        graph = {str(f'{UPPER_VERTEX}{k[0]}'):[] for k in J_equal}
        for i in J_equal:
            graph[str(f'{UPPER_VERTEX}{i[0]}')].append(str(f'{LOWER_VERTEX}{i[1]}'))

        max_pair_list, graph = bipartite_max_matching(graph)

        if len(max_pair_list) == n:
            return [(int(v.replace(UPPER_VERTEX, '')), int(u.replace(LOWER_VERTEX, '')))
                    for (v, u) in max_pair_list]

        start_v = set(f'{UPPER_VERTEX}{i}' for i in range(n)) - set(i for (i, j) in max_pair_list)
        v_star = set()
        for v in start_v:
            v_star = v_star.union(dfs(set(), graph, v))
        I_star = set(int(v.replace(UPPER_VERTEX, '')) for v in v_star if UPPER_VERTEX in v)
        J_star = set(int(u.replace(LOWER_VERTEX, '')) for u in v_star if LOWER_VERTEX in u)

        alphas_capped = [1 if i in I_star else -1 for i in range(n)]
        betas_capped = [-1 if i in J_star else 1 for i in range(n)]
        theta = min((c[i, j] - alphas[i] - betas[j]) / 2 for i in I_star for j in set(range(n)) - J_star)

        alphas = [alpha + theta * alphas_capped[i] for i, alpha in enumerate(alphas)]
        betas = [beta + theta * betas_capped[i] for i, beta in enumerate(betas)]


if __name__ == '__main__':
    C = np.array([
        [7, 2, 1, 9, 4],
        [9, 6, 9, 5, 5],
        [3, 8, 3, 1, 8],
        [7, 9, 4, 2, 2],
        [8, 4, 7, 4, 8],
    ])

    indexes = dual_based_proc(C)
    print('Indexes: ', indexes)
    print(sum(C[i, j] for (i, j) in indexes))
