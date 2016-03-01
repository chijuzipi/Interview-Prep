def find(root, target):
    out = []
    helper(root, target, out)
    return out

def helper(root, target, out):
    if root.val == target:
        out.append([root])

    map = {}
    left  = helper(root.left, target, out)
    right = helper(root.right, target, out)
    for l in left.keys():
        for r in right.keys():
            if root.val + l + r == target:
                buildPath(left[l], root.val, right)

