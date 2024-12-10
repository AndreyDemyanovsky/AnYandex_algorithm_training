from collections import deque

number_of_rovers = int(input())
result = [None] * number_of_rovers
m_road1, m_road2 = map(int, input().split())
if m_road1 in (1, 4) and m_road2 in (1, 4):
    pr = [4, 1, 2, 3]
elif not m_road1 in (1, 4) and not m_road2 in (1, 4):
    pr = [2, 3, 4, 1]
else:
    s = {1, 2, 3, 4}.difference((m_road1, m_road2))
    pr = [min(m_road1, m_road2), max(m_road1, m_road2), min(s), max(s)]

pr = [i - 1 for i in pr]
events = []

roads = [deque(), deque(), deque(), deque()]

for i in range(number_of_rovers):
    d, t = map(int, input().split())
    events.append([t, d - 1, i])
events.sort()

for i in events:
    roads[i[1]].append(i)

while any(roads):    
    t = min((i[0][0] for i in roads if i))

    for n in range(len(pr)):
        i = pr[n]
        next_i = pr[n + 1] if n not in (3, 1) else None

        if roads[i] and roads[i][0][0] == t:
            rover = roads[i].popleft()

            if next_i and roads[next_i] and roads[next_i][0][0] == t\
                  and abs(rover[1] - roads[next_i][0][1]) == 2: 
                next_rover = roads[next_i].popleft()
                result[next_rover[2]] = t

            result[rover[2]] = t
            t += 1
            break

    for i in roads:
        if i and i[0][0] < t:
            i[0][0] = t 

for i in result:
    print(i)
