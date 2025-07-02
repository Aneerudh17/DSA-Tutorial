class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

result = []

def preorder(root):
    if not root:
        return []
    
    #access the root value first
    result.append(root.val)

    #access the left subtree values
    preorder(root.left)
    
    #access the right subtree values
    preorder(root.right)
    return result