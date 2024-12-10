def get_permutations_brackets(n, permutation=None, stack=None, all_permutation=None):
    if not permutation:
        permutation = []

    if not all_permutation:
        all_permutation = []

    if not stack:
        stack = []

    if n == 0:
        if not stack:
            all_permutation.append("".join(permutation))
        return all_permutation

    dict_brackets = ["(", "[", ")", "]"]

    d = {")": "(", "]": "["}

    for bracket in dict_brackets:
        if bracket in ("(", "[") and len(stack) != n:
            stack.append(bracket)
            permutation.append(bracket)
            all_permutation = get_permutations_brackets(n - 1, permutation, stack, all_permutation)
            permutation.pop()
            stack.pop()
        elif bracket in (")", "]") and stack and stack[-1] == d[bracket]:
            delt = stack.pop()
            permutation.append(bracket)
            all_permutation = get_permutations_brackets(n - 1, permutation, stack, all_permutation)
            permutation.pop()
            stack.append(delt)

    return all_permutation


N = int(input())
if N % 2 == 0:
    print(*get_permutations_brackets(N), sep="\n")