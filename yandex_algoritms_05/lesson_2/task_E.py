number_berries = int(input())
good_ber = []
bad_ber = []

maxi_good = None
maxi_bad = None


def f(obj, mx, flag="good"):
    res = None
    if not mx:
        res = obj
    elif flag == "good":
        res = obj if obj.down > mx.down else mx
    elif flag == "bad":
        res = obj if obj.up > mx.up else mx
    return res


class Berrie:
    def __init__(self, up, down, number):
        self.up = up
        self.down = down
        self.dif = up - down
        self.number = number


for i in range(number_berries):
    up, down = map(int, input().split())
    new_berri = Berrie(up, down, i + 1)

    if up - down >= 0:
        good_ber.append(new_berri)
        maxi_good = f(new_berri, maxi_good)
    else:
        bad_ber.append(new_berri)
        maxi_bad = f(new_berri, maxi_bad, "bad")

answer = []
max_h = 0
for berri in good_ber:
    if berri is not maxi_good:
        max_h += berri.dif
        answer.append(berri.number)

if maxi_good and maxi_bad:
    if maxi_good.up < maxi_good.dif + maxi_bad.up:
        answer.append(maxi_good.number)
        answer.append(maxi_bad.number)
        max_h += maxi_good.dif + maxi_bad.up
    else:
        answer.append(maxi_good.number)
        max_h += maxi_good.up
        maxi_bad = None
elif maxi_good:
    answer.append(maxi_good.number)
    max_h += maxi_good.up
else:
    answer.append(maxi_bad.number)
    max_h += maxi_bad.up


for berri in bad_ber:
    if berri is not maxi_bad:
        answer.append(berri.number)


print(max_h)
print(*answer)
