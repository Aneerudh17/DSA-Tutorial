#the goal is to find the length of the linked list
#traverse till the end of the linked list and have a counter
#return the counter

#implementing
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def length(head):
    if not head:
        counter = 0
        return counter
    else:
        counter = 1
        current = head
        while current.next:
            counter += 1
            current = current.next
        return counter
#example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(length(head))