def solution():
    list_numbers = list(map(int, input().split()))

    first_big = list_numbers[0]
    second_big = list_numbers[1]

    first_smal = list_numbers[0]
    second_smal = list_numbers[1]

    for i in range(2, len(list_numbers)):
        el = list_numbers[i]
        if second_big < first_big:
            second_big, first_big = first_big, second_big
        
        if second_smal > first_smal:
            second_smal, first_smal = first_smal, second_smal


        if el >= second_big:
            first_big = second_big
            second_big  = el
        elif  el >= first_big:
            first_big = el
        
        if el <= second_smal:
            first_smal = second_smal
            second_smal = el
        elif el <= first_smal:
            first_smal = el
                

    if first_big * second_big < first_smal * second_smal:
        res1, res2 = second_smal, first_smal
    else:
        res1, res2 = first_big, second_big

    if res1 > res2:
        res1, res2 = res2, res1

    return res1, res2

print(*solution())