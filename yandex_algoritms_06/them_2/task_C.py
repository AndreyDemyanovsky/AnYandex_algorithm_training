number_of_monuments, min_distance = map(int, input().split())
list_distance = list(map(int, input().split()))

l = 0
r = 1
number_of_possible_ways = 0

def check_stipulation(gr, le):
    return gr - le > min_distance

while r < len(list_distance):
    if check_stipulation(list_distance[r], list_distance[l]):
        number_of_possible_ways += len(list_distance) - r
        l += 1
    else:
        r += 1

print(number_of_possible_ways)

