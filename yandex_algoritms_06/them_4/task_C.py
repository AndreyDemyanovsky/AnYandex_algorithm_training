import sys
sys.setrecursionlimit(100000)
f = open("input.txt", "r")
number_elements = int(f.readline()) - 1
WOOD = {}
CHILD_PARENT = {}
requests = []

set_p = set()
set_c = set()
for i in f:
    if  number_elements > 0:
        child, parent = i.split()
        CHILD_PARENT[child] = parent
        WOOD.setdefault(parent, []).append(child)
        set_c.add(child)
        set_p.add(parent)
    else:
        nodeA, nodeB = i.split()
        requests.append((nodeA, nodeB))
    number_elements -= 1

root, *_ = set_p.difference(set_c)

def get_depths(tree, root, d=0, result=None):
    if result is None:
        result = {}
    result[root] = d
    if root in tree:
        for node in tree[root]:
            get_depths(tree, node, d + 1, result)
    return result

depths = get_depths(WOOD, root)

def get_LCA(nodeA, nodeB):

    depth_A = depths[nodeA]
    depth_B = depths[nodeB]

    if depth_A > depth_B:
        nodeA, nodeB = nodeB, nodeA
        depth_A, depth_B = depth_B, depth_A
    
    while depth_A != depth_B:
        nodeB = CHILD_PARENT[nodeB]
        depth_B -= 1
    
    while nodeA != nodeB:
        nodeA = CHILD_PARENT[nodeA]
        nodeB = CHILD_PARENT[nodeB]
    print(nodeA)

for request in requests:
    nodeA, nodeB = request
    get_LCA(nodeA, nodeB)
    