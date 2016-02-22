'''
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the
first greater element on the right side of x in array. Elements for which no greater element exist, consider next
greater element as -1.

Examples:
a) For any array, rightmost element always has next greater element as -1.
b) For an array which is sorted in decreasing order, all elements have next greater element as -1.
c) For the input array [4, 5, 2, 25], the next greater elements for each element are as follows.

if involve locality of 1-dimensional array, consider stack
'''
'''
--> corner case
1) nums
2) 
'''

def next(nums):
    if not nums or len(nums) == 0:
        return []
    s = []
    out = [-1 for x in range(len(nums))]
    s.append((nums[0], 0))
    for i in range(len(nums)):
        while s and nums[i] > s[-1][0]:
            index = s.pop()
            out[index[1]] = nums[i]
        s.append((nums[i], i))
    return out
    
nums = [1, 2]
print next(nums)

