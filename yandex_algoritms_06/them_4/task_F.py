import sys
sys.setrecursionlimit(300000)
NUMBER_EMPLOYEES = int(input())
ROOT = 1
NUMBER_BOSS_i_EMPLOUEES = map(int, input().split())
number_coins = [1] * NUMBER_EMPLOYEES
tree: dict[int, list[int]] = {}
number_descendants: dict[int, int] = {}

for ind, value in enumerate(NUMBER_BOSS_i_EMPLOUEES):
    tree.setdefault(value, []).append(ind + 2)


def get_depths(node):
    count = 0
    if node in tree:
        for i in tree[node]:
            count += get_depths(i)
    number_descendants[node] = count
    return number_descendants[node] + 1

get_depths(ROOT)

def get_coins(node):
    summa = 0
    if node in tree:
        for i in tree[node]:
            summa += get_coins(i)
    number_coins[node - 1] += summa + number_descendants[node]
    return number_coins[node - 1]

get_coins(ROOT)
print(*number_coins)