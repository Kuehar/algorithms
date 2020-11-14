class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def storeinorderInSet(root,s):
    if not root:
        return 
    
    storeinorderInSet(root.left,s)
    s.add(root.data)
    storeinorderInSet(root.right,s)

def setToBST(s,root):
    if not root:
        return 
    
    setToBST(s,root.left)
    it = next(iter(s))
    root.data = it
    s.remove(it)
    setToBST(s,root.right)

def binaryTreeToBST(root):
    s = set()

    storeinorderInSet(root,s)
    setToBST(s,root)



def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.data,end = " ")
    inorder(root.right)

if __name__ == "__main__":
    pass