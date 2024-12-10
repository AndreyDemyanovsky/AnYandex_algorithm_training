n, l = map(int, input().split())


def get_seq(x1, d1, a, c, m):
    s = [x1]
    d = d1
    for _ in range(l-1):
        s.append(s[-1] + d)
        d = (a * d + c) % m
    return s


seq = []
for _ in range(n):
    seq.append(get_seq(*map(int, input().split())))


def check(element, target, flag=None):
    if flag == "less":
        return element >= target
    if flag == "more":
        return element > target
    return None


def find(lf, rg, lst, t, flag):
    while lf < rg:
        m = (lf + rg) // 2
        if check(lst[m], t, flag):
            rg = m
        else:
            lf = m + 1

    return lf if flag == "less" else len(lst) - lf


def search(seq1, seq2):
    left = min(seq1[0], seq2[0])
    right = max(seq2[-1], seq2[-1])

    while left < right:
        mid = (left + right) // 2
        less = find(0, l, seq1, mid, "less") + find(0, l, seq2, mid, "less")
        more = find(0, l, seq1, mid, "more") + find(0, l, seq2, mid, "more")
        if less <= l-1 and more <= l:
            return mid
        elif more > l:
            left = mid + 1
        elif less > l - 1:
            right = mid - 1

    return left


for i in range(n):
    for j in range(i + 1, n):
        print(search(seq[i], seq[j]))

