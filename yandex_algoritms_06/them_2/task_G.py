length_string, max_rudeness = map(int, input().split())
string = input()
number_a = 0
number_b = 0
l = 0
length = 0
rudeness = 0

for r in range(length_string):
    if string[r] == "a":
            number_a += 1
    elif string[r] == "b":
        number_b += 1
        if number_a > 0:
            rudeness += number_a

    if rudeness > max_rudeness:
        while string[l] != "a":
            if string[l] == "b":
                number_b -= 1
            l += 1
        l += 1
        number_a -= 1
        rudeness -= number_b

    if r - l + 1 > length:
        length = r - l + 1

print(length)