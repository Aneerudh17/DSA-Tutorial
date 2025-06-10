#initializing a node
class Node:
    def __init__(self,data):
        self.data = data # data is passed as an arguement
        self.next = None # initially the next of a node is set to None


class LinkedList:
    def __init__(self):
        self.head = None

#inserting in a linked list

    #inserting at the beginning of a linked list
    def insertAtBegin(self,data):
        new_node = Node(data)
        if not self.head: #check if the head node is present or not
            self.head = new_node #if head node is not present the new node becomes the head node
        
        else:
            new_node.next = self.head # if head node is present the new_node is added before the head node
            self.head = new_node # now the new node becomes the head node

    #inserting at the end of the linked list    
    def insertAtEnd(self,data):
        new_node = Node(data) 
        if not self.head: #check if the head node is present or not
            self.head = new_node #if the head node is not present the new node becomes the head node

        else:
            currentnode = self.head #if the head node exist traverse till the last node
            while currentnode.next: #usually done by traversing until we find a node with next = None
                currentnode = currentnode.next
            
            currentnode.next = new_node #once found link the next to the newnode
    
    #inserting at a specific position
    def insertAtIndex(self,data,index):
        new_node = Node(data)
        if index == 0:
            self.insertAtBegin(data) #if head is not present => InsertAtBegin

        else:
            position = 0 #initialising a position variable to keep track of the position
            currentnode = self.head #initialising a currentnode to move the nodes to the required index
            while currentnode != None and position+1 != index: #using position+1 so it is one node behind
                position += 1 #increasing the position counter
                currentnode = currentnode.next #moving the node by one
            
            if currentnode != None: 
                new_node = Node(data)
                new_node.next = currentnode.next
                currentnode.next = new_node
            else:
                print("index not present")
    
    #updating the node of a linked list
    def updateNode(self,val,index):
        currentnode = self.head 
        position = 0 
        if position == index:
            currentnode.data = val #if the nodes that needs to be updated if the first node, then change the value directly
        else:
            while currentnode != None and position+1 != index: #traverse till you find the right index
                position += 1
                currentnode = currentnode.next #move the node by one position
            if currentnode != None: 
                currentnode.data = val #after finding the index change the value
            else:
                print("index not present")

#deleting the nodes
    #deleting the first node
    def deleteAtBeg(self):
        if not self.head:
            return
        else:
            self.head = self.head.next
    
    #deleting the last node
    def deleteAtEnd(self):
        if not self.head:
            return
        
        else:
            currentnode = self.head.next
            previousnode = self.head
            while currentnode != None:
                currentnode = currentnode.next
                previousnode = currentnode

            previousnode.next = None
    #deleting a node at a specific index
    def deleteAtIndex(self,index):

        if not self.head:
            return
        if index == 0:
            self.deleteAtBeg()
        else:
            currentnode = self.head.next
            previousnode = currentnode
            position = 0
            while currentnode is not None and position +1 != index:
                previousnode.next = currentnode.next
                currentnode.next = None
