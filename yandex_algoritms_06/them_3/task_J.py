from collections import deque

number_chairs, Vasyi_height = map(int, input().split())
height_chairs = list(map(int, input().split()))
wight_chairs = list(map(int, input().split()))
sorted_chairs = sorted(zip(height_chairs, wight_chairs))

min_inconvenience = float("inf")
que = deque()
wight = 0
left_pointer = 0
is_breake = False

for i in range(number_chairs):

    wight += sorted_chairs[i][1]
    
    if  0 < i:
        inconvenience = abs(sorted_chairs[i - 1][0] - sorted_chairs[i][0])
        while que and que[-1][0] < inconvenience:
            que.pop()
        que.append((inconvenience, i - 1))

    while wight >= Vasyi_height:
        if not que:
            min_inconvenience = 0
            is_breake = True
            break
        elif que[0][0] < min_inconvenience:
            min_inconvenience = que[0][0]

        if left_pointer == que[0][1]:
            que.popleft()
        wight -= sorted_chairs[left_pointer][1]
        left_pointer += 1

    if is_breake:
        break
        
print(min_inconvenience) 
