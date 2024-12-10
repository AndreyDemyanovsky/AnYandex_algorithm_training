import sys
sys.setrecursionlimit(100000)


class Node:
    def __init__(self, value):
        self.key = value
        self.child = {}
        self.parent = False

    def add_child(self, ch):
        self.child[ch.key] = ch


class Tree:
    def __init__(self):
        self.tree = {}

    def add_node(self, parent: str, son: str):
        if parent not in self.tree:
            self.tree[parent] = Node(parent)
        if son not in self.tree:
            self.tree[son] = Node(son)

        self.tree[son].parent = True
        self.tree[parent].add_child(self.tree[son])

    def in_tree(self, key):
        return key in self.tree

    def get_root(self):
        for name in self.tree:
            if self.tree[name].parent is False:
                return self.tree[name]

    def set_number_descendants(self, node=None):
        if not node:
            node = self.get_root()
        n_des = 0
        for son in list(node.child.values()):
            n_des += self.set_number_descendants(son)

        node.n_descendants = n_des
        return n_des + 1

    def print_number_descendants(self):
        for name in sorted(self.tree.keys()):
            obj = self.tree[name]
            print(obj.key, obj.n_descendants)


N = int(input())
tree = Tree()

for _ in range(N - 1):
    son, parent = input().split()
    tree.add_node(parent, son)

tree.set_number_descendants()
tree.print_number_descendants()