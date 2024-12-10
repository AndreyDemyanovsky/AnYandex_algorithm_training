# P - дерево где стоит вася  V - спустя сколько деревьев у него высохнет краска
# Q - дерево где стоит Маша M - спустя сколько деревьев засохнет краска у Маши
P, V = map(int, input().split())
Q, M = map(int, input().split())


def f(point_v, stamina_v, point_m, stamina_m):

    maxim_v = point_v + stamina_v
    minim_v = point_v - stamina_v

    maxim_m = point_m + stamina_m
    minim_m = point_m - stamina_m
    if maxim_v >= maxim_m >= minim_v or maxim_m >= maxim_v >= minim_m:
        return max(maxim_v, maxim_m) - min(minim_v, minim_m) + 1
    return (maxim_v - minim_v + 1) + (maxim_m - minim_m + 1)

print(f(P, V, Q, M))