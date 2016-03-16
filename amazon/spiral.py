'''
spiral order visit of a matrix

-->two method
--> corner case:
1) nums
2) only one element?
'''

def spiral(nums):
    if not nums or len(nums) == 0 or len(nums[0]) == 0:
        return []

    h = len(nums)
    w = len(nums[0])
    total = h * w
    res = []
    res.append(nums[0][0])
    i = 0
    j = 0
    layer = 0
    while len(res) < total:
        while j + 1 < w-layer and len(res) < total:
            j += 1
            res.append(nums[i][j])
        while i + 1 < h-layer and len(res) < total:
            i += 1
            res.append(nums[i][j])
        while j-1 >= layer and len(res) < total:
            j -= 1 
            res.append(nums[i][j])
        while i-1 > layer and len(res) < total:
            i -= 1
            res.append(nums[i][j])

        layer += 1
    return res

def spiral(nums):
    if not nums or len(nums) == 0 or len(nums[0]) == 0:
        return []
    rowT = len(nums)
    colT = len(nums[0])
    rowS = 0
    colS = 0
    out = []
    while rowS < rowT and colS < colT:
        if rowS < rowT and colS < colT:
            for i in range(colS, colT):
                out.append(nums[rowS][i])
            rowS += 1

        if rowS < rowT and colS < colT:
            for i in range(rowS, rowT):
                out.append(nums[i][colT-1])
            colT -= 1

        if rowS < rowT and colS < colT:
            for i in range(colT-1, colS-1, -1):
                out.append(nums[rowT-1][i])
            rowT -= 1

        if rowS < rowT and colS < colT:
            for i in range(rowT-1, rowS-1, -1):
                out.append(nums[i][colS])
            colS += 1
    return out

nums = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
print spiral(nums)
            
