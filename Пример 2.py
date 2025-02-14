class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def add_children(self, *args):
        for child in args:
            self.add_child(child)
    def __repr__(self):
        return f"<{self.value}>"
# Построение дерева
root = TreeNode("dir")
root.add_child(TreeNode("dir2"))
root.add_child(TreeNode("dir3"))
root.children[0].add_child(TreeNode("file4"))
root.children[1].add_child(TreeNode("file5"))
root.children[1].add_child(TreeNode("file6"))
# Цель поиска
goal = "file5"