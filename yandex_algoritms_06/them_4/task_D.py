class Node:
    def __init__(self, value):
        self._value = value
        self._left_son = None
        self._right_son = None

    @property
    def value(self):
        return self._value

    @property
    def left_son(self):
        return self._left_son
    
    @left_son.setter
    def left_son(self, new_value):
        self._left_son = new_value

    @property
    def right_son(self):
        return self._right_son

    @right_son.setter
    def right_son(self, new_value):
        self._right_son = new_value

    
class BinarySearchTree:

    def __init__(self):
        self._root = None

    def add(self, new_node: Node):

        if self.search(new_node.value) == "YES":
            print("ALREADY")
        elif self._root is None:
            self._root = new_node
            print("DONE")
        else:
            node = self._root
            while True:
                if new_node.value < node.value:
                    if node.left_son is None:
                        node.left_son = new_node
                        break
                    node = node.left_son
                else:
                    if node.right_son is None:
                        node.right_son = new_node
                        break
                    node = node.right_son
            print("DONE")  

    def search(self, target):
        node = self._root

        while node:
            if target < node.value:
                node = node.left_son
            elif target > node.value:
                node = node.right_son
            else:
                return "YES"
        return "NO"

    def print_ree(self):
        def bypass(node, depth=0):
            if node.left_son:
                bypass(node.left_son, depth + 1)
            print("." * depth + str(node.value))
            if node.right_son:
                bypass(node.right_son, depth + 1)
        bypass(self._root)

tree = BinarySearchTree()

for request in open("input.txt", "r"):
    command, *n = request.split()
    n = map(int, n)
    match command:
        case "ADD":
            obj = Node(*n)
            tree.add(obj)
        case "SEARCH":
            print(tree.search(*n))
        case "PRINTTREE":
            tree.print_ree()