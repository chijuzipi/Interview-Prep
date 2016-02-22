'''
Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf
nodes interchanged.

followup: Given an n-ary tree convert it to its mirror image.

'''
'''
--> corner case
1) root == None


'''
def mirrorBTree(root):
    if root == None:
        return root
    left = mirrorTree(root.left)
    right = mirrorTree(root.right)
    root.left  = right
    root.right = left
    return root
    

def mirrorNTree(root):
    if root == None:
        return root
    temp = []
    for child in root.childern:
        temp.append(mirrorNTree(child)
    temp.reverse()
    root.children = temp
    return root
        
