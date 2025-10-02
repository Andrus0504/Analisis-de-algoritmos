def isSafe(vertex, graph, path, pos):
    if not graph[path[pos - 1]][vertex]:
        return False
    
    for i in range(pos):
        if path[i] == vertex:
            return False
    return True

def hamCycleUtil(graph, path, pos, n):
    if pos == n:
        return graph[path[pos - 1]][path[0]]
    for v in range(1, n):
        if isSafe(v, graph, path, pos):
            path[pos] = v
            if hamCycleUtil(graph, path, pos + 1, n):
                return True
            path[pos] = -1
        return False
    
def hamCycle(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0
    if not hamCycleUtil(graph, path, 1, n):
        return [-1]
    return path

if __name__ == "main":
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]

    path = hamCycle(graph)
    if path[0] == -1:
        print("No existe solucion")
    else:
        for i in range(len(path)):
            print(path[i], end=" ")
            print(path[0])