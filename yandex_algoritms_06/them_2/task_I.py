number_of_algorithms = int(input())
interest_of_algorithms = list(map(int, input().split()))
usefulness_of_algorithms = list(map(int, input().split()))
mood_next_days = list(map(int, input().split()))


def get_sorted_tuple(sequence_one, sequence_two):
    result = []
    for i  in range(number_of_algorithms):
        result.append((sequence_one[i], sequence_two[i], -i))
    result.sort(reverse=True)
    return result

interest = get_sorted_tuple(interest_of_algorithms, usefulness_of_algorithms)
useful = get_sorted_tuple(usefulness_of_algorithms, interest_of_algorithms)

i_interest = 0
i_useful = 0
set_index = set()
result = []

for i in mood_next_days:
    if i:
        ind = abs(useful[i_useful][2])
        while ind in set_index:
            i_useful += 1
            ind = abs(useful[i_useful][2])
        set_index.add(ind)
        result.append(ind + 1)
        i_useful += 1
    else:
        ind = abs(interest[i_interest][2])
        while ind in set_index:
            i_interest += 1
            ind = abs(interest[i_interest][2])
        set_index.add(ind)
        result.append(ind + 1)
        i_interest += 1

print(*result)

