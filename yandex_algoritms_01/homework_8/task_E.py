list_num = list(map(int, input().split()))


class Tree:
    def __init__(self):
        self.root = None

    def _add_(self, node, node_tree):

        if node.value < node_tree.value:
            if node_tree.left_son is None:
                node_tree.left_son = node
                node.parent = node_tree
            else:
                self._add_(node, node_tree.left_son)

        elif node.value > node_tree.value:
            if node_tree.right_son is None:
                node_tree.right_son = node
                node.parent = node_tree
            else:
                self._add_(node, node_tree.right_son)

    def add_node(self, new_node):
        if self.root is None:
            self.root = new_node
            self.root.node_depth = 1
        elif not self.search(new_node, self.root):
            self._add_(new_node, self.root)

    def search(self, search_node, node_tree):
        ans = False
        if node_tree is None:
            return False

        if node_tree.value == search_node.value:
            return True
        elif search_node.value < node_tree.value:
            ans = self.search(search_node, node_tree.left_son)
        elif search_node.value > node_tree.value:
            ans = self.search(search_node, node_tree.right_son)
        return ans

    def print_sorted_sheet(self, node):
        if not node.left_son and not node.right_son:
            print(node.value)

        if node.left_son:
            self.print_sorted_sheet(node.left_son)
        if node.right_son:
            self.print_sorted_sheet(node.right_son)


class Node:
    def __init__(self, value):
        self.value = value
        self.left_son = None
        self.right_son = None
        self.parent = None


tree = Tree()
for i in list_num:
    if i != 0:
        node = Node(i)
        tree.add_node(node)

tree.print_sorted_sheet(tree.root)