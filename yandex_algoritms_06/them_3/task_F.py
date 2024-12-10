n = int(input())
PRIORITY_BR = {v: i + 1 for i, v in enumerate(input())}
START_STRING = input()
end_string = []
REVERSE_BR = {"(": ")", "[": "]", ")": "(", "]": "["}

i = 0
stack = []
while i < n:
    if i < len(START_STRING):
        if START_STRING[i] in ("(["):
            stack.append(START_STRING[i])
        else:
            stack.pop()
    else:
        if len(stack) + 2 <= n - i:
            min_open_br = min(PRIORITY_BR["("], PRIORITY_BR["["])
            if not stack or min_open_br < PRIORITY_BR[REVERSE_BR[stack[-1]]]:
                br = "(" if min_open_br == PRIORITY_BR["("] else "["
                stack.append(br)
                end_string.append(br)
            else:
                br = REVERSE_BR[stack[-1]]
                stack.pop()
                end_string.append(br)
        else:
            end_string.append(REVERSE_BR[stack[-1]])
            stack.pop()
    i += 1

print(START_STRING + "".join(end_string))
                




    
