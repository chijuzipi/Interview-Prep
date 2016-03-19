'''
The question divided into 2 levels:

1) given an unsorted array with a group of charcters, find the first occurance of non-repeating character

2) Find the first non-repeating character from a stream of characters Given a stream of characters, find the first non-repeating character from stream. You need to tell the first non-repeating character in O(1) time at any moment.

-->

corner case:
1) all show once
2) all repeating

'''

def find1(strs):
    map = {}
    for c in strs:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1
    for c in strs:
        if map[c] == 1:
            return c
        
def find2(stream):
    root = Node(0) 
    tail = Node(0)
    root.right = tail
    tail.left  = root
    curr = root
    map = {}
    def get():
        right = root.right
        if right == tail:
            return None
        return right

    def remove(node):
        if not node:
            return 
        left = node.left
        right= node.right
        left.right = right
        right.left = left

    for c in stream:
        if c in map:
            remove(map[c])
            map[c] = None
        else:
            node = Node(c)
            left = tail.left
            left.right = node
            node.left = left
            node.right = tail
            tail.left = node
            map[c] = node
        printNode(root)

def printNode(root):
    print 
    while root:
        print root.x, 
        root = root.right

class Node(object):
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right= None

find2('abadbf') 
find2('aabb') 


