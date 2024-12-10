balls, n_people = map(int, input().split())
events = []


def create_events(t, z, y, i):
    ev = []
    count_ball = time = 0
    balls_before_rest = z
    while count_ball != balls:
        if balls_before_rest == 0:
            balls_before_rest = z
            time = time + y
        else:
            balls_before_rest -= 1
            count_ball += 1
            time += t
            ev.append((time, i))
    return ev


for i in range(n_people):
    T, Z, Y = map(int, input().split())
    events.extend(create_events(T, Z, Y, i))
events.sort()

all_time = 0
res = [0] * n_people
count_balls = 0

pointer_event = 0
while count_balls != balls:
    event = events[pointer_event]
    count_balls += 1
    pointer_event += 1
    res[event[1]] += 1
    all_time = event[0]

print(all_time)
print(*res)