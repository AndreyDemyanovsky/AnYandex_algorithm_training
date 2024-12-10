k = int(input())
s = input()

pointer = k
ways = 0
prev_l = 0
while pointer < len(s):
    if s[pointer] == s[pointer - k]:
        prev_l += 1
        ways += prev_l
    else:
        prev_l = 0
    pointer += 1
print(ways)
