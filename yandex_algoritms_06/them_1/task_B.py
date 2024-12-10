A = int(input()) # синие майки
B = int(input()) # красные майки
C = int(input()) # синие носки
D = int(input()) # красные носки

tshirt_blue = B + 1
tshirt_red = A + 1

socks_blue = D + 1
socks_red = C + 1

if 0 in (B, D):
    print(tshirt_blue, socks_blue)
elif 0 in (A, C):
    print(tshirt_red, socks_red)
elif (r:= min(max(tshirt_blue, tshirt_red), max(socks_blue, socks_red))) \
    < tshirt_blue + socks_blue and r < tshirt_red + socks_red:

    if r in (tshirt_blue, tshirt_red):
        print(r, 1)
    else:
        print(1, r)

elif tshirt_blue + socks_blue <= tshirt_red + socks_red:
    print(tshirt_blue, socks_blue)
elif tshirt_blue + socks_blue > tshirt_red + socks_red:
    print(tshirt_red, socks_red)