count_turtle = int(input())
turtles_with_conscience = set()

for _ in range(1, count_turtle + 1):
    turtles_after_i, turtles_before_i = map(int, input().split())

    if turtles_after_i >= 0 and turtles_before_i >= 0  and turtles_after_i + turtles_before_i == count_turtle - 1:
        turtles_with_conscience.add((turtles_after_i, turtles_before_i))
    
print(len(turtles_with_conscience))