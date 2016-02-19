'''
flip coin to get the longest streak of 1s
-->
corner:
1) nums == None or len(nums) == 0
2) no 0s in nums
3) other element aside from 1 and 0

'''

class Solution(object):
    def flip(self, nums):
        
        temp = [float('-inf') for x in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                temp[i] = scan(nums, i) 
        out = max(temp)+1 
        if out == float('-inf'):
            return len(nums)
        return out

def scan(nums, i):
    l = i-1
    r = i+1
    count = 0
    while l >= 0 and nums[l] == 1:
        count += 1
        l -= 1
    while r < len(nums) and nums[r] == 1:
        count += 1
        r += 1
    return count

if __name__ == "__main__":
    nums = [1]
    print Solution().flip(nums)

        
