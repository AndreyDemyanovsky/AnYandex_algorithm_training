# координаты юго-западного
x1 = int(input())
y1 = int(input())
# координаты северо-восточного угла
x2 = int(input())
y2 = int(input())
# координаты пловца
x = int(input())
y = int(input())


if y > y2:
    if x > x2:
        print("NE")
    elif x < x1:
        print("NW")
    else:
        print("N")
elif y < y1:
    if x > x2:
        print("SE")
    elif x < x1:
        print("SW")
    else:
        print("S")
else:
    if x < x1:
        print("W")
    else:
        print("E")