N = int(input())


def generate_numbers(n: int, remaining_numbers, prefix=None):
    if not remaining_numbers:
        print("".join(map(str, prefix)))
        return
    prefix = prefix or []

    for i in range(1, n + 1):
        if i in remaining_numbers:
            prefix.append(i)
            remaining_numbers.remove(i)
            generate_numbers(n, remaining_numbers, prefix)
            remaining_numbers.append(i)
            prefix.remove(i)


generate_numbers(N, [i for i in range(1, N + 1)])