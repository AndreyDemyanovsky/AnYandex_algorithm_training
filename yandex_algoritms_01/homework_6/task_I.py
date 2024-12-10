n, team, n_in_team = map(int, input().split())

list_people = [int(input()) for _ in range(n)]
list_people.sort()


def get_number_team(dif_height):
    lf = 0
    rg = n_in_team
    count_team = 0
    while rg <= n:
        if list_people[rg - 1] - list_people[lf] <= dif_height:
            lf = rg
            rg = lf + n_in_team
            count_team += 1
        else:
            lf += 1
            rg += 1
    return count_team


def search(left, right):
    while left < right:
        mid = (left + right) // 2
        if get_number_team(mid) >= team:
            right = mid
        else:
            left = mid + 1
    return left


print(search(0, 999_999_999))