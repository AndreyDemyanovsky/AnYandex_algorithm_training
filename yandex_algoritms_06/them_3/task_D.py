expression = [int(i) if i.isdigit() else i for i in input().split()]
stack = []

for i in expression:
    if type(i) == int:
        stack.append(i)
    else:
        res = None
        sn = stack.pop()
        fn = stack.pop()
        match i:
            case "+":
                res = fn + sn
            case "-":
                res = fn - sn
            case "*":
                res = fn * sn
        stack.append(res)
print(*stack)
