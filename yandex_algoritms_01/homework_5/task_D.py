n_monuments, distance_vision = map(int, input().split())
monuments = list(map(int, input().split()))
point_one = point_two = 0

distance = 0
possible_ways = 0
while point_two < n_monuments:
    distance = monuments[point_two] - monuments[point_one]

    if distance > distance_vision:
        possible_ways += n_monuments - point_two
        point_one += 1
    else:
        point_two += 1

print(possible_ways)