number_office = int(input())
employees_in_office = list(map(int, input().split()))
ind_last_office = len(employees_in_office) - 1

def get_last_total_number_of_transitions(employees_in_office, reverse=False):
    summa_in_last_office = 0
    if reverse:
        for i in range(ind_last_office, 0, -1):
            summa_in_last_office += employees_in_office[i] * abs(0 - i)
    else:
        for i in range(ind_last_office):
            summa_in_last_office += employees_in_office[i] * (ind_last_office - i)
    return summa_in_last_office

summa_in_last_right = get_last_total_number_of_transitions(employees_in_office)
summa_in_last_left = get_last_total_number_of_transitions(employees_in_office, True)

def get_prefix_sum(employees_in_office):
    prefix_sum = [0]
    for i in range(len(employees_in_office)):
        new_prefix_sum = employees_in_office[i] + prefix_sum[-1]
        prefix_sum.append(new_prefix_sum)
    return prefix_sum

prefix_sum_in_right = get_prefix_sum(employees_in_office)
employees_in_office.reverse()
prefix_sum_in_left = get_prefix_sum(employees_in_office)
prefix_sum_in_left.reverse()
employees_in_office.reverse()

result_in_left = [summa_in_last_left]
for i in range(1, ind_last_office + 1):
    summa_in_last_left -= prefix_sum_in_left[i]
    result_in_left.append(summa_in_last_left)

result_in_right = [summa_in_last_right]
for i in range(ind_last_office - 1, -1, -1):
    summa_in_last_right -= prefix_sum_in_right[i + 1]
    result_in_right.append(summa_in_last_right)
result_in_right.reverse()

min_transitions = None
for i in range(len(result_in_left)):
    if not min_transitions:
        min_transitions = result_in_left[i] + result_in_right[i]
    elif min_transitions > (s := result_in_left[i] + result_in_right[i]):
        min_transitions = s

print(min_transitions)
