class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

result = []

def postorder(root):
    if not root:
        return []
    
    #access the left subtree values
    postorder(root.left)
    
    #access the right subtree values
    postorder(root.right)

    #access the root value
    result.append(root.val)
    return result