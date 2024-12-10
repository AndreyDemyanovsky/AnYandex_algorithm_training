A, B, C, D, E = (int(input()) for _ in range(5))
big_edge_hole = max(D, E)
small_edge_hole = D if big_edge_hole == E else E

small_edge_brick = min(A, B, C)
middle_edge_brick = None
match small_edge_brick:
    case n if n == A:
        middle_edge_brick = B if B <= C else C
    case n if n == B:
        middle_edge_brick = A if A <= C else C
    case n if n == C:
        middle_edge_brick = A if A <= B else B

flag = "NO"
if small_edge_brick <= small_edge_hole and middle_edge_brick <= big_edge_hole:
    flag = "YES"

print(flag)