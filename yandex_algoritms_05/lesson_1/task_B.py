fc_game1, sc_game1 = map(int, input().split(":"))
fc_game2, sc_game2 = map(int, input().split(":"))
home = int(input())

if fc_game1 + fc_game2 > sc_game1 + sc_game2:
    print(0)

elif fc_game1 + fc_game2 < sc_game1 + sc_game2:
    df = (sc_game1 + sc_game2) - (fc_game1 + fc_game2)
    if home == 1:
        if df + fc_game2 == sc_game1:
            print(df + 1)
        elif df + fc_game2 < sc_game1:
            print(sc_game1 - (df + fc_game2) + 1)
        else:
            print(df)
    if home == 2:
        if fc_game1 > sc_game2:
            print(df)
        elif fc_game1 <= sc_game2:
            print(df + 1)

else:
    if home == 2:
        if fc_game1 <= sc_game2:
            print(1)
        else:
            print(0)

    if home == 1:
        if fc_game2 <= sc_game1:
            print(1)
        else:
            print(0)
