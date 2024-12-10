N = int(input())
events = []

first_day = 0
last_day = 1


def get_number_days(year, mouth, days):
    number_days = 0
    number_days += days
    mouth_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, year):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            number_days += 366
        else:
            number_days += 365

    for i in range(mouth):
        number_days += mouth_days[i]
        if i == 1 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            number_days += 1
    return number_days


for i in range(N):
    day1, mount1, year1, day2, mount2, year2 = map(int, input().split())
    count_days_when_turned_18 = get_number_days(year1 + 18, mount1, day1)
    count_days_when_died = get_number_days(year2, mount2, day2 - 1)
    count_days_when_turned_80 = get_number_days(year1 + 80, mount1, day1 - 1)

    if count_days_when_turned_18 <= count_days_when_died:
        events.append((count_days_when_turned_18, 0, i + 1))

        if count_days_when_died > count_days_when_turned_80:
            events.append((count_days_when_turned_80, 1, i + 1))
        else:
            events.append((count_days_when_died, 1, i + 1))

events.sort()


answer = False
group = set()
new_set = None
for _, _type_, number in events:
    if _type_ == first_day:
        group.add(number)
        new_set = True
    else:
        if new_set:
            answer = True
            print(*group)
            new_set = False
        group.remove(number)

if not answer:
    print(0)