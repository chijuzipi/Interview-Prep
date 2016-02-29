'''
given an unsorted array with a group of charcters, fin dthe first occurance of non-repeating character.

-->
corner case:
1) all show once
2) all repeating

'''

def find(s):
    map = {}
    root = Node(0)
    curr = root
    for i in range(len(s)):
        char = s[i]
        if char in map:
            #print 'here', char
            node = map[char]
            removeNode(node, curr)
        else:
            node = Node(char)
            map[char] = node
            curr.right = node
            node.left = curr
            curr = curr.right

    return root.right.val

def printNode(root):
    curr = root.right
    while curr:
        print curr.val
        curr = curr.right
    
def removeNode(node, curr):
    if node.left == None:
        return 
    if node != curr:
        node.left.right = node.right
        node.right.left = node.left
        node.right = None
        node.left  = None
    else:
        curr = node.left
        node.left.right = None
        node.left = None

class Node(object):
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None
    

print find('zabasd')

