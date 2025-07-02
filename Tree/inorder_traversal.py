class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

result = []

def inorder(root):
    if not root:
        return []
    
    #access the left subtree first
    inorder(root.left)
    #access the root
    result.append(root.val)
    #access the right subtree
    inorder(root.right)
    return result