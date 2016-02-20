'''
flip coin to get the longest streak of 1s
-->
corner:
1) nums == None or len(nums) == 0
2) no 0s in nums
3) other element aside from 1 and 0: assumption no
4) k == 0

'''

class Solution(object):
    def flipOne(self, nums):
        
        temp = [float('-inf') for x in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                temp[i] = scan(nums, i) 
        out = max(temp)+1 
        if out == float('-inf'):
            return len(nums)
        return out

    def flipK(self, nums, k):
        if nums == None or len(nums) == 0:
            return 0
        s = 0
        f = 0
        count = 0
        maxi = 0
        while f < len(nums):
            while f < len(nums) and count <= k:
                maxi = max(maxi,  f-s)
                if nums[f] == 0:
                    count += 1
                f += 1

            if count <= k:
                maxi = max(maxi,  f-s)

            while s < len(nums) and s <= f and count > k:
                if nums[s] == 0:
                    count -= 1
                s += 1

        return maxi
            
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
    nums = [1,1,0,0,1,1,1,0,1,1,0,1]
    print Solution().flipOne(nums)
    print Solution().flipK(nums, 2)

        
