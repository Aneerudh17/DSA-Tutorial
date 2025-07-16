class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root,result= None):
    if result is None:
        result = []
    
    if not root:
        return result
    #access the root value first
    result.append(root.val)

    #access the left subtree values
    preorder(root.left,result)
    
    #access the right subtree values
    preorder(root.right,result)
    return result

#sample usage
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")

root.left.left = TreeNode("D")
root.left.left.left = TreeNode("H")
root.left.left.right = TreeNode("I")

root.left.right = TreeNode("E")
root.left.right.left = TreeNode("J")
root.left.right.right = TreeNode("K")

root.right.left = TreeNode("F")
root.right.left.left = TreeNode("L")
root.right.left.right = TreeNode("M")

root.right.right = TreeNode("G")
root.right.right.left = TreeNode("N")
root.right.right.right = TreeNode("O")

print(preorder(root))