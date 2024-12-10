import heapq


def main():
    n = int(input())
    vertex_start, vertex_end = map(int, input().split())
    r = int(input())
    bus_routes = [[] for i in range(n + 1)]

    for i in range(r):
        start_village, time_departure, final_village, time_arrival = map(int, input().split())
        bus_routes[start_village].append((time_departure, final_village, time_arrival,))

    heap = [(0, vertex_start)]
    heapq.heapify(heap)
    dist = [float('inf')] * (n + 1)
    visit = [False] * (n + 1)
    dist[vertex_start] = 0

    while heap:
        weight_first_node, first_node = heapq.heappop(heap)
        if not visit[first_node]:
            visit[first_node] = True
            for time_departure, second_node, time_arrival in bus_routes[first_node]:
                if time_arrival < dist[second_node] and dist[first_node] <= time_departure:
                    dist[second_node] = time_arrival
                    heapq.heappush(heap, (time_arrival, second_node))

    print(dist[vertex_end] if visit[vertex_end] else -1)


main()