'''
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 =
c2.

Example:

Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.
'''
'''
--> corner case:
1) nums == None len(nums) == 0
2) less than 3 element
3) zero: OK

'''

class Solution(object):
    def find(self, nums):
        if not nums or len(nums) < 3:
            return False
        temp = []
        for num in nums:
            temp.append(num * num)
        
        temp.sort()
        i = len(temp)-1
        while i > 1:
            target = temp[i]
            if check(temp, target, i-1):
                return True
            i -= 1
        return False

def check(temp, target, r):
    l = 0
    while l < r:
        summ = temp[l] + temp[r]
        if summ == target:
            return True
        elif summ < target:
            l += 1
        else:
            r -= 1
    return False

if __name__ == "__main__":
    nums1 = [3, 1, 4, 6, 5]
    nums2 = [10, 4, 6, 12, 5]
    print Solution().find(nums1)
    print Solution().find(nums2)






