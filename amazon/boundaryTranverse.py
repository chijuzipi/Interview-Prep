'''
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.

-->
1) print root
2) print root.left (only print left node, not the last one)
3) print root.left (only print leaf node)
4) print root.right(only print leaf node)
5) print root.right(only print rightnode, not the last one)

--> 
corner case:
1) root == None

'''

def boundary(root):
    if root:
        print (root.val)
    else:
        return 
        
    node = root
    while node.left and node.left.left:
        node = node.left
        print node.val
    printleaf(root.left, 1)
    printleaf(root.right, -1)
    printright(root.right)

def printright(node):
    if not node:
        return 
    if node.right:
        printright(node.right)
    if node.left == None and node.right == None:
        return 
    print node.val

def printleaf(node, order):
    if not node:
        return
    if node.left == None and node.right == None:
        print node.val
        return 
    if order == 1:
        printleaf(node.left, 1)
        printleaf(node.right, 1)
    else:
        printleaf(node.right, -1)
        printleaf(node.left, -1)

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.right = Node(25)
boundary(root)

