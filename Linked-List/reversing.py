class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse(head):
    prev = None
    current = head

    while current:
        next = current.next #save the next node
        current.next = prev #reverse the links
        prev = current #change prev node
        current = next #move the pointer to the next node

    return prev

#printing the linked list
def printlist(head):
    current = head
    while current:
        print(current.val, end= "->" if current.next else "")
        current = current.next
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
printlist(head)
#output : 1->2->3
reversed_head = reverse(head)
printlist(reversed_head)
#output : 3->2->1
