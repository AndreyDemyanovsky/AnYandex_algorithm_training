N = int(input())
counter_ticket_office = 0
OPEN, CLOSE = (1, 0)
events = []

for _ in range(N):
    hour1, minutes1, hour2, minutes2 = map(int, input().split())
    minutes_open = hour1 * 60 + minutes1
    minutes_close = hour2 * 60 + minutes2

    if minutes_open >= minutes_close:
        events.append((0, OPEN))
        events.append((minutes_close, CLOSE))
        events.append((minutes_open, OPEN))
        events.append((24 * 60, CLOSE))
    else:
        events.append((minutes_open, OPEN))
        events.append((minutes_close, CLOSE))

events.sort()
result = 0
for i in range(len(events)):
    event = events[i]
    if event[1] == OPEN:
        counter_ticket_office += 1
    elif event[1] == CLOSE:
        if counter_ticket_office == N:
            result += event[0] - events[i - 1][0]
        counter_ticket_office -= 1

print(result)