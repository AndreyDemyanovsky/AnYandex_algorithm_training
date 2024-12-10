import sys
sys.setrecursionlimit(100000)
NUMBER_ELEMENTS: int = int(input()) - 1
WOOD: dict[str, list[str]] = {}

set_p: set[str] = set()
set_c: set[str] = set()
for _ in range(NUMBER_ELEMENTS):
    child, parent = input().split()
    WOOD.setdefault(parent, []).append(child)
    WOOD.setdefault(child, [])
    set_c.add(child)
    set_p.add(parent)

root, *_ = set_p.difference(set_c)

def get_number_descendants(wood, root, result=None):
    if result is None:
        result = []
    
    s = 0
    if wood[root]:
        for i in wood[root]:
            result, s_prev = get_number_descendants(wood, i, result)
            s += s_prev
    result.append(f"{root} {s}")
    return result, s + 1

result, _ = get_number_descendants(WOOD, root)
for i in sorted(result):
    print(i)