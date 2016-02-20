'''
Q-4 There are two linked lists. Both linked lists have a single-digit number in their nodes. I needed to
treat this linked lists as a numbers and add them up and store the digits in a new linked list.
E.g., head -> 5 -> 6 -> 7-> 9
head -> 2-> 1 -> 1
Resultant linked list: head-> 5 -> 8-> 9-> 0 (5679 + 211 = 5890)

-->
corner case:
1) linkedlist is None: yes
2) non-digit exist: assume no
3) linkedlist has cycle: assume no
4) singlely linked? : assume yes
'''
class Solution(object):
    def addlinkedlist(self, head1, head2):
        if head1 == None or head1.next == None:
            return head2
        if head2 == None or head2.next == None:
            return head1
        newhead1 = reverse(head1)
        newhead2 = reverse(head2)
        res = add(newhead1, newhead2)
        return reverse(res)

def reverse(head):
    if head == None or head.next == None:
        return head
    s = head
    f = head.next
    while f:
        temp = f.next
        f.next = s
        s = f
        f = temp
    head.next = None
    return s

def add(head1, head2):
    root  = Node(None)
    curr  = root
    carry = 0
    while head1 or head2 or carry:
        num1 = head1.val if head1 else 0
        num2 = head2.val if head2 else 0
        res = num1 + num2 + carry 
        digit = res % 10
        carry = digit / 10
        curr.append(Node(digit))
        curr = curr.next
    return root.next
        

    
