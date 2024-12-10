interval_trains_1 = int(input())
interval_trains_2 = int(input())
count_trains_1 = int(input())
count_trains_2 = int(input())

min_1 = count_trains_1 + ((count_trains_1 - 1) * interval_trains_1)
max_1 = count_trains_1 + ((count_trains_1 + 1) * interval_trains_1)

min_2 = count_trains_2 + ((count_trains_2 - 1) * interval_trains_2)
max_2 = count_trains_2 + ((count_trains_2 + 1) * interval_trains_2)


min_from_min = max(min_1, min_2)
max_from_max = min(max_1, max_2)

if min_from_min <= max_from_max:
    print(min_from_min, max_from_max)
else:
    print(-1)