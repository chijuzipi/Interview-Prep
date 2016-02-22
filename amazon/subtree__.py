'''
Q-8 Given two trees, find out if the second tree is a “subtree” of the first one.

--> 
algorithm:
1) check substring of inorder and preorder
2) when do tranversal, append "#" when encounter None

corner case:
1) root1 is None or root2 is None or both None

time: O(n+m), space O(n+m)
'''



