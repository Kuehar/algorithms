class BinaryTreeNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

    def tree_traversal(root):
        if root:
            # Preorder
            print("Preorder: %d" % root.left)
            tree_traversal(root.left)

            print("Inorder: %d" % root.data)
            tree_traversal(root.right)

            print("Postorder: %d" % root.data)