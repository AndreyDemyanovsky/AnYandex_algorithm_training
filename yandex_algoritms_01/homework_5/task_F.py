n = int(input())
min_power_for_i_class = list(map(int, input().split()))
min_power_for_i_class.sort()

m = int(input())
models_conditioner = [tuple(map(int, input().split())) for _ in range(m)]
models_conditioner.sort(key=lambda x: x[1])

summa = 0
pointer = 0
for i in min_power_for_i_class:

    while models_conditioner[pointer][0] < i:
        pointer += 1
    summa += models_conditioner[pointer][1]

print(summa)