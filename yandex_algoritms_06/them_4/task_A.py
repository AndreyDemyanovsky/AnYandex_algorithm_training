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

def go(wood, root, hight=0, result=None):
    if result is None:
        result = []

    for i in wood[root]:
        result = go(wood, i, hight + 1, result)
    result.append(f"{root} {str(hight)}")
    return result

for i in sorted(go(WOOD, root)):
    print(i)

    




