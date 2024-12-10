import sys
sys.setrecursionlimit(100000)
NUMBER_VERTICES = int(input())
tree = {}
visit = [False] * NUMBER_VERTICES

for _ in range(NUMBER_VERTICES - 1):
    parent, child = map(int, input().split())
    tree.setdefault(parent, []).append(child)
    tree.setdefault(child, []).append(parent)

result = {}
def get_nubmer_descendants(root=1):        
    summa = 1
    visit[root - 1] = True
    for i in tree[root]:
        if not visit[i - 1]:
            summa += get_nubmer_descendants(i)
    result[root] = summa 
    return summa

get_nubmer_descendants()

print(*(result[key] for key in sorted(result.keys())))
