expression = input()
    
def get(exp):
    last = None
    operation_pr = {"+": 1, "-": 1, "*": 2}
    result = []
    stack = []
    set_ = set("0123456789+-*() ")

    i = 0
    while i < len(exp):
        s = exp[i]

        if s not in set_:
            return False
    
        if s.isdigit():
            if last and last not in ("(", "operation"):
                return False
                
            j = i
            while i < len(exp) and exp[i].isdigit():
                i += 1

            result.append(int(exp[j:i]))
            last = "digit"
            continue

        elif s == ")":
            if not stack or last == "operation":
                return False
            print()    
            while stack[-1] != "(":
                result.append(stack.pop())
                if not stack:
                    return False
            stack.pop()
            last = ")"

        elif s == "(":
            if last and last not in (")", "(", "operation"):
                return False

            stack.append("(")
            last = "("

        elif s in "+-*":
            if not last or last not in ("digit", ")") or i == len(exp) - 1:
                return False

            while stack and stack[-1] != "(" and operation_pr[s] <= operation_pr[stack[-1]]:
                elem = stack.pop()
                result.append(elem)
            stack.append(s)
            last = "operation"

        i += 1
    stack.reverse()
    result.extend(stack)
    return result


var = get(expression)
if var:
    stack = []
    
    for i in var:
        if type(i) == int:
            stack.append(i)
        else:
            res = None
            sn = stack.pop()
            if not stack:
                print("WRONG")
                break
            fn = stack.pop()
            match i:
                case "+":
                    res = fn + sn
                case "-":
                    res = fn - sn
                case "*":
                    res = fn * sn
            stack.append(res)
    else:
        print(*stack)
else:
    print("WRONG")



# def check_bracket_and_valid_characters(string):
#     bracket = 0
#     valid_set = set("0123456789+-*() ")

#     for i in string:
#         if i not in valid_set:
#             return False
#         if i == "(":
#             bracket += 1
#         elif i == ")":
#             bracket -= 1
#             if bracket < 0:
#                 return False
#     if bracket != 0:
#         return False
#     return True
