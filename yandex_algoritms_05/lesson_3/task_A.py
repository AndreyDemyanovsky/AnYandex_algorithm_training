number_peoples = int(input())

set_songs = None

for _ in range(number_peoples):
    k = int(input())
    if not set_songs:
        set_songs = set(input().split())
    else:
        set_songs = set_songs.intersection(set(input().split()))


print(len(set_songs))
print(*sorted(set_songs))