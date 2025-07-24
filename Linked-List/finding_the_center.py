#goal is to find the center of the linked list using fast and slow pointers
#the fast pointer moves twice as fast as the slow pointer
#when the fast pointer reaches the end , the slow pointer will be at the middle of the linked list

#implementaion
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def middle(head):
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def printlist(head):
    current = head
    while current:
        print(current.val,end="->" if current.next else "")
        current = current.next
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
printlist(head)

listmiddle = middle(head)
print(listmiddle.val)