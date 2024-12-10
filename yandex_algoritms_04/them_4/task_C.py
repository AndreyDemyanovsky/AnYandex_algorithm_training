N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def incision_for_permutation(permutation, gr, n):
    incision = 0
    visit = [True] * n
    for i in range(n - 1):
        for j in range(n):
            if visit[j] and permutation[i] != permutation[j]:
                incision += gr[i][j]
        visit[i] = False
    return incision


def get_max_incision(n, gr):
    result = 0
    list_groups = []
    for i in range(int((2 ** n) // 2), (2 ** n) - 1):
        number_zeros = n - len(bin(i)[2:])
        pref = "0" * number_zeros
        binary_representation_number = list(map(lambda group: int(group) + 1, pref + bin(i)[2:]))
        x = incision_for_permutation(binary_representation_number, gr, n)
        if x >= result:
            result = x
            list_groups = binary_representation_number

    return result, list_groups


total_edge_weight, groups = get_max_incision(N, graph)
print(total_edge_weight)
print(*groups)