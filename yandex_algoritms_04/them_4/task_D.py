N = int(input())

graph = []
min_wight = []

for i in range(N):
    minimum = float("inf")
    lst_wight = []
    for value in map(int, input().split()):
        lst_wight.append(value)
        if value != 0 and value < minimum:
            minimum = value
    graph.append(lst_wight)
    min_wight.append(minimum)


# greedy algorithm for finding a possible path
def get_best(matrix, n):
    visit = [False] * n
    i = 0
    best = 0

    while True:
        visit[i] = True
        next_vertex = None
        minimum = float("inf")

        for ind, value in enumerate(matrix[i]):
            if not visit[ind] and 0 < value < minimum:
                minimum = value
                next_vertex = ind
        if not next_vertex:
            if not all(visit):
                return -1
            else:
                best += matrix[i][0]
                return best
        i = next_vertex
        best += minimum


def min_route(n, adjacency_matrix, lst_min_weight, index_vertex=0, lenght_route=0, best=None, appraisal=None, visit=None):

    if not visit:
        visit = [False] * n
        visit[index_vertex] = True
    if not best:
        best = get_best(adjacency_matrix, n)
        if best == -1:
            return best
    if all(visit) and lenght_route + adjacency_matrix[index_vertex][0] <= best:
        return lenght_route + adjacency_matrix[index_vertex][0]
    if not appraisal:
        appraisal = sum(lst_min_weight) - lst_min_weight[index_vertex]

    for ind, value in enumerate(adjacency_matrix[index_vertex]):
        if 0 < value and not visit[ind] and not lenght_route + value + appraisal >= best:
            visit[ind] = True
            lenght_route += value
            appraisal -= lst_min_weight[ind]
            best = min_route(n, adjacency_matrix, lst_min_weight, ind, lenght_route, best, appraisal, visit)
            visit[ind] = False
            lenght_route -= value
            appraisal += lst_min_weight[ind]

    return best


print(min_route(N, graph, min_wight))