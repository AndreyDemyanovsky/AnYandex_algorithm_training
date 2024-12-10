x, y, z = map(int, input().split())

n = int(input())
numbers_n = set()


while n != 0:
    last = n % 10
    numbers_n.add(last)
    n = n // 10

set_xyz = set((x, y, z))

print(len(numbers_n.difference(set_xyz)))