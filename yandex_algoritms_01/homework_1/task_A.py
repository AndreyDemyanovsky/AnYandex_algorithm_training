troom, tcond = map(int, input().split())
mod = input()

match mod:
    case "freeze":
        if troom > tcond:
            print(tcond)
        else:
            print(troom)
    case "heat":
        if troom < tcond:
            print(tcond)
        else:
            print(troom)
    case "auto":
        print(tcond)
    case "fan":
        print(troom)