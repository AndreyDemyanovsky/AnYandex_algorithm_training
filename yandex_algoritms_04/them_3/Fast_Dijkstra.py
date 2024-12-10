import heapq


def main():
    n, k = map(int, input().split())
    edges = [[] for i in range(n + 1)]

    for i in range(k):
        first_vertex, second_vertex, weight = map(int, input().split())
        edges[first_vertex].append((second_vertex, weight))
        edges[second_vertex].append((first_vertex, weight))

    vertex_start, vertex_end = map(int, input().split())
    heap = [(0, vertex_start)]
    heapq.heapify(heap)
    dist = [float('inf')] * (n + 1)
    visit = [False] * (n + 1)
    dist[vertex_start] = 0

    while heap:
        weight_first_node, first_node = heapq.heappop(heap)

        if not visit[first_node]:
            visit[first_node] = True
            for second_node, cost_path in edges[first_node]:
                all_path = weight_first_node + cost_path
                if all_path < dist[second_node]:
                    dist[second_node] = all_path
                    heapq.heappush(heap, (all_path, second_node))

    print(dist[vertex_end] if visit[vertex_end] else -1)


main()