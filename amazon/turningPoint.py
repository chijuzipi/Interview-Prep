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
4) all the same element?
'''

def solve(nums):
    if len(nums) <= 2:
        return linear(nums)
    l = 0
    r = len(nums)-1
    while l < r:
        m = (l+r)/2
        if nums[m] >= nums[m-1] and nums[m] >= nums[m+1]:
            return nums[m]
        elif nums[m] < nums[m-1]:
            r = m-1
        else:
            l = m+1

    return -1

def linear(nums):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return nums[i]
    return -1

nums = [1, 1, 1,1,1]
print solve(nums)
