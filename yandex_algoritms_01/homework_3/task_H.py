count_birds = int(input())

count_shots = set()
for _ in range(count_birds):
    x, y = map(int, input().split())
    count_shots.add(x)

print(len(count_shots))