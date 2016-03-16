'''
Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

Example
Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2

'''
def find(nums):
    if not nums or len(nums) == 0:
        return -1
    h = len(nums)
    w = len(nums[0])
    maxi = 0
    maxiRow = 0
    for i in range(h):
        index = helper(nums, i, 0, w-1)
        if w-index > maxi:
            maxi = w-index
            maxiRow = i
            
    return maxiRow, maxi

def helper(nums, row, l, r):
    if l > r:
        return l
    m = (l+r) / 2
    if nums[row][m] >= 1:
        return helper(nums, row, l, m-1)
    else:
        return helper(nums, row, m+1, r)

#nums = [[1,1,1,1], [1, 1, 1, 1], [1,1,1,1], [0,0,0,0]]
nums = [[0]]
print find(nums)
