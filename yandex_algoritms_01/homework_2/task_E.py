n = int(input())
competitions_participants = [int(i) for i in input().split()]
points_v = 0
one_of_winners = max(competitions_participants)
flag = False

for i in range(len(competitions_participants) - 1):
    participant_points = competitions_participants[i]
    participant_poins_after = competitions_participants[i + 1]

    if not flag and participant_points == one_of_winners:
        flag = True
    elif flag and participant_points % 10 == 5 and participant_poins_after < participant_points and points_v < participant_points: 
        points_v = participant_points

place_competitions = 0
if points_v:
    for i in competitions_participants:
        if i > points_v:
            place_competitions += 1
    else:
        place_competitions += 1

print(place_competitions)
