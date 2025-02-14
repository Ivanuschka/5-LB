class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def add_children(self, left, right):
            self.left = left
            self.right = right
    def __repr__(self):
        return f"<{self.value}>"
# Построение дерева
root = BinaryTreeNode(1)
left_child = BinaryTreeNode(2)
right_child = BinaryTreeNode(3)
root.add_children(left_child, right_child)
right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))
# Целевое значение
goal = 4