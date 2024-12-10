n = int(input())
number_of_clicks = 0

for _ in range(n):
    number_of_spaces = int(input())

    if number_of_spaces > 4:
        remainder = number_of_spaces % 4
        without_remainder = number_of_spaces - remainder
        count_four_in_number = number_of_spaces // 4

        s1 = remainder + count_four_in_number
        s2 = without_remainder + 4 - number_of_spaces + (count_four_in_number + 1)
        number_of_clicks += s1 if s1 < s2 else s2

    else:
        s1 = number_of_spaces
        s2 = 4 - number_of_spaces + 1
        if s1 < s2:
            number_of_clicks += s1
        else:
            number_of_clicks += s2

print(number_of_clicks)

