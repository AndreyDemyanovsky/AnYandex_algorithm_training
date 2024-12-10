def main():
    n, start, end = map(int, input().split())
    init_vertex = start
    max_weight = 30000
    graf = [([0] * (n + 1)) if i == 0 else [0] + list(map(int, input().split())) for i in range(n + 1)]
    visit = [False] * (n + 1)
    dist = [max_weight] * (n + 1)
    dist[init_vertex] = 0
    prev_vertex = [None] * (n + 1)
    prev_vertex[init_vertex] = init_vertex

    while not visit[end]:
        visit[init_vertex] = True

        for i in range(1, len(graf[init_vertex])):
            summa_road = graf[init_vertex][i] + dist[init_vertex]
            if graf[init_vertex][i] > 0 and summa_road and summa_road < dist[i]:
                dist[i] = summa_road
                prev_vertex[i] = init_vertex

        new_vertex = None
        k = 30000
        for i in range(len(dist)):
            if dist[i] < k and not visit[i]:
                new_vertex = i
                k = dist[i]
        init_vertex = new_vertex

        if init_vertex is None:
            break

    if visit[end]:
        road = [end]
        while end != start:
            end = prev_vertex[end]
            road.append(end)

        road.reverse()
        print(*road)
    else:
        print(-1)


main()
