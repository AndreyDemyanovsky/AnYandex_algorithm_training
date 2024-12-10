N = int(input())
list_ropes = list(map(int, input().split()))
mx = max(list_ropes)
save = mx
for i in list_ropes:
    if i != save:
        mx -= i

if mx <= 0 or mx == save:
    print(sum(list_ropes))
else:
    print(mx)
