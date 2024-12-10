n1 = int(input())
lst_1 = list(map(int, input().split()))

n2 = int(input())
lst_2 = list(map(int, input().split()))

n3 = int(input())
lst_3 = list(map(int, input().split()))

set_1 = set(lst_1)
set_2 = set(lst_2)
set_3 = set(lst_3)

res = set()
res = res.union(set_1.intersection(set_2))
res = res.union(set_1.intersection(set_3))
res = res.union(set_2.intersection(set_3))
print(*sorted(res))