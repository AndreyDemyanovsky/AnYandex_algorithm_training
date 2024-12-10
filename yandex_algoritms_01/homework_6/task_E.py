deuces = int(input())
threes = int(input())
fours = int(input())
summa = (deuces * 2 + threes * 3 + fours * 4)
n_estimates = deuces + threes + fours


def get_average(count_fives):
    s = summa + (5 * count_fives)
    n = n_estimates + count_fives
    return s * 2 >= n * 7  # правило пропорций


def binsearch(left_border, right_border):
    while left_border < right_border:
        count_fives = (left_border + right_border) // 2
        if get_average(count_fives):
            right_border = count_fives
        else:
            left_border = count_fives + 1
    return left_border


print(binsearch(0, 10 ** 17))
