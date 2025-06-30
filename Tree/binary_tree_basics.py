class Treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
        
    print(node.data)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def InOrderTraversal(node):
    if node is None:
        return
    
    InOrderTraversal(node.left)
    print(node.data)
    InOrderTraversal(node.right)



root = Treenode("R")
nodeA = Treenode("A")
nodeB = Treenode("B")
nodeC = Treenode("C")
nodeD = Treenode("D")
nodeE = Treenode("E")
nodeF = Treenode("F")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

print(root.right.left.data)
preOrderTraversal(root)
print("inorder traversal")
InOrderTraversal(root)