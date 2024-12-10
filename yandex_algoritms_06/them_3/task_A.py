bracketed_sequence = input()
answer = "yes" if len(bracketed_sequence) >= 2 else "no"
stack = []
revers_bracketed = {")": "(", "]": "[", "}": "{"}
for i in bracketed_sequence:
    if i in ("(", "[", "{"):
        stack.append(i)
    else:
        if not stack or stack[-1] != revers_bracketed[i]:
            answer = "no"
            break
        stack.pop()
if stack:
    answer = "no" 
print(answer)

