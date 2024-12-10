N, K, M = map(int, input().split())
count = 0
while N >= K >= M:
    N = N - K
    count += K // M
    N += K % M
    if N < K:
        break
print(count)