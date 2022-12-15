from itertools import zip_longest
from itertools import chain

ADD_VERT = 'S'


def dfs(visited: list, graph: dict, finish_v: list, node: str) -> (list, bool):
    if node not in visited:
        visited.append(node)
    if node in finish_v:
        return visited, True

    for adjacent in (x for x in graph[node] if x not in visited):
        if dfs(visited, graph, finish_v, adjacent)[1] is True:
            return visited, True

    visited.remove(node)
    return visited, False


def two_part_max_matching(graph: dict) -> list:
    M = []
    V = set(graph.keys())
    U = set(chain.from_iterable(graph.values()))

    while True:
        start_v = set((i for i in V if not [item for item in M if i in item]))
        finish_v = set((i for i in U if not [item for item in M if i in item]))

        if len(start_v) == 0 or len(finish_v) == 0:
            return M, graph
        elif len(start_v) > 1:
            graph[ADD_VERT] = list(start_v)
            dfs_starting_v = ADD_VERT
        else:
            dfs_starting_v = start_v.pop()

        additional_vertexes, flag = dfs(list(), graph, finish_v, dfs_starting_v)

        if flag is False:
            return M, graph

        if ADD_VERT in additional_vertexes:
            additional_vertexes.remove(ADD_VERT)
            graph.pop(ADD_VERT)

        additional_chain = list(zip_longest(additional_vertexes[0::2], additional_vertexes[1::2])) \
                              + list(zip_longest(additional_vertexes[1::2], additional_vertexes[2::2]))
        additional_chain = [edge for edge in additional_chain if not any(elem is None for elem in edge)]

        for edge in additional_chain:
            if edge[0] in graph.keys():
                graph[edge[0]].remove(edge[1])
                if edge[1] not in graph.keys():
                    graph[edge[1]] = list()
                graph[edge[1]].append(edge[0])
            if (edge[1], edge[0]) in M:
                M.remove((edge[1], edge[0]))
            else:
                M.append(edge)


def maximal_matching():
    graph = {
        'v1': ['u1'],
        'v2': ['u1', 'u2'],
        'v3': ['u1', 'u2', 'u3'],
    }

    max_matching, g = two_part_max_matching(graph)
    print("possible maximal matching: ", max_matching)


if __name__ == '__main__':
    maximal_matching()
