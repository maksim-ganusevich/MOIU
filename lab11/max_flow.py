def restore_path(l: dict, start: str, finish: str) -> list:
    cur_idx = finish
    path = []
    while cur_idx != start:
        path.append(l[cur_idx])
        cur_idx = l[cur_idx][0]
    return path


def mark_f_f(G_f: dict, start: str, finish: str):
    Q = [start]
    l = {start: None}
    while len(Q) != 0 and finish not in l:
        cur_v = Q.pop(0)
        for u in filter(lambda v: v[0] == cur_v, G_f.keys()):
            if u[1] not in l:
                l[u[1]] = u
                Q.append(u[1])
    return l


def ford_fulkerson(graph: dict, start: str, finish: str) -> dict:
    G = {(k, e[0]): 0 for k, v in graph.items() for e in v}
    G_f = {(k, e[0]): e[1] for k, v in graph.items() for e in v}
    G_f.update({(k[1], k[0]): 0 for k in G_f.keys() if (k[1], k[0]) not in G_f.keys()})

    while True:
        l = mark_f_f(dict(filter(lambda val: val[1] != 0, G_f.items())), start, finish)

        if finish not in l:
            return G

        cur_vertexes = restore_path(l, start, finish)
        theta = min(dict(filter(lambda val: val[0] in cur_vertexes, G_f.items())).values())
        for v in cur_vertexes:
            G[v] = G[v] + theta
            G_f[v] = G_f[v] - theta
            G_f[(v[1], v[0])] = G_f[(v[1], v[0])] + theta


def start_f_f():
    graph = {
        '1': [('2', 3), ('3', 2)],
        '2': [('4', 1), ('3', 2)],
        '3': [('4', 2)],
    }
    start = '1'
    finish = '4'

    max_flow = ford_fulkerson(graph, start, finish)
    max_flow_value = sum(v for k, v in max_flow.items() if k[0] == start)
    print("Max flow: {}, flow: {}".format(max_flow_value, max_flow))


if __name__ == '__main__':
    start_f_f()


