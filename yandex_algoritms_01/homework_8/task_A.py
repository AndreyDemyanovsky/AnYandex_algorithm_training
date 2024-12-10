list_num = list(map(int, input().split()))


class Tree:
    def __init__(self):
        self.root = None

    def _add_(self, node, node_tree):

        if node.value < node_tree.value:
            if node_tree.left_son is None:
                node_tree.left_son = node
            else:
                self._add_(node, node_tree.left_son)

        elif node.value > node_tree.value:
            if node_tree.right_son is None:
                node_tree.right_son = node
            else:
                self._add_(node, node_tree.right_son)

    def add_node(self, new_node):
        if self.root is None:
            self.root = new_node
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

    def get_deep(self, node, mx_deep=0):
        if not node.right_son and not node.left_son:
            return mx_deep + 1
        result = 0
        if node.left_son:
            mx_deep += 1
            r = self.get_deep(node.left_son, mx_deep)
            result = max(result, r)
            mx_deep -= 1
        if node.right_son:
            mx_deep += 1
            r = self.get_deep(node.right_son, mx_deep)
            result = max(result, r)
            mx_deep -= 1
        return result


class Node:
    def __init__(self, value):
        self.value = value
        self.left_son = None
        self.right_son = None


tree = Tree()
for i in list_num:
    if i != 0:
        tree.add_node(Node(i))

print(tree.get_deep(tree.root))