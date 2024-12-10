a1, b1, a2, b2 = map(int, input().split())

if b1 > a1:
    a1, b1 = b1, a1

if b2 > a2:
    a2, b2 = b2, a2

if a2 > a1:
    a1, b1, a2, b2 = a2, b2, a1, b1

s1 = a1 * (b1 + b2)

s2 = (max(b1, a2) * (a1 + b2))

if s1 < s2:
    print(a1, (b1 + b2))
else:
    print(max(b1, a2), (a1 + b2))
