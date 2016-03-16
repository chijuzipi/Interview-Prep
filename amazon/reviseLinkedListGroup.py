'''
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3 
Output:  3->2->1->6->5->4->8->7->NULL. 

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL. 

'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head, k):
    if not head or not head.next:
        return head
    root = ListNode(0)     
    root.next = head
    f = head
    pre = root
    post = None
    while f:
        count = k
        while f and count>1:
            f = f.next
            count -= 1
        if not f:
            break
        start = pre.next
        post = f.next if f else None
        if f:
            f.next = None
        newhead = reverse(start)
        pre.next = newhead
        start.next = post
        pre = start
        f = post
    return root.next


def reverse(head):
    if not head or not head.next:
        return head
    f = head.next
    s = head
    while f:
        temp = f.next
        f.next = s
        s = f
        f = temp
    head.next = None
    return s

def printList(head):
    print 
    while head:
        print head.val, 
        head = head.next

prev = None
head = None
for i in range(1, 9):
    node = ListNode(i)
    if prev:
        prev.next = node
    else:
        head = node
    prev = node

#printList(head)
printList(reverseList(head, 3))


