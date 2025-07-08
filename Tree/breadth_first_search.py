#returning nodes in level order
#implementation using queue
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
def bfs(root):
    if not root:
        return
        
    queue = [root]

    while queue:
        node = queue.pop(0) # dequeuing the first item in the list (thats how queue works)
        print(node.val, end=" ")

        #checking if there is a left node
        if node.left:
            queue.append(node.left)

        #check if there is a right node
        if node.right:
            queue.append(node.right)
        #it loops untill there are no more nodes left in the queue
        
#sample usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

bfs(root)

            