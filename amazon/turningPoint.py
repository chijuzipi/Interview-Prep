'''
given an array of integers where the number go increasingly and at a point will start decreasing something like the
following.

2 3 4 5 6 7 8 6 4 3 2.

we need to find the turning point of this series. in this example it is 8.
'''

'''
--> corner case:
1) nums == None len(nums) == 0
2) no turning point: assume no
3) duplicate value: assume yes
'''

def solve(nums):
    if not nums or len(nums) == 0:
        return -1
    l = 0
    r = len(nums)-1
    while r-l > 1:
        m = (l+r)/2
        if nums[m] >= nums[l]:
            l = m
        else:
            r = m

    return nums[l]

nums = [2, 3,  4,  5,  6,  7,  8,  6,  4,  3,  2]
print solve(nums)
