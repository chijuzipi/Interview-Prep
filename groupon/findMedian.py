'''
find median of two array with the same length
'''
from random import randint
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == l2 and l1 == 2:
            return mergeMedian(nums1, nums2)

        m1 = findm(nums1)
        m2 = findm(nums2)

        newnums1 = []
        newnums2 = []
        if m1 == m2:
            return m1
        elif m1 > m2:
            newnums1 = nums1[:l1/2+1]
            newnums2 = nums2[l2/2:]

            return self.findMedianSortedArrays(newnums1, newnums2)
        else:
            newnums1 = nums1[l1/2:]
            newnums2 = nums2[:l2/2+1]
                
            return self.findMedianSortedArrays(newnums1, newnums2)
    
def findm(nums):
    l = len(nums)
    if len(nums) % 2 == 0:
        return (float(nums[l/2]) + float(nums[l/2-1]))/2
    else:
        return nums[l/2]

def mergeMedian(nums1, nums2):
    return (float(max(nums1[0], nums2[0])) + float(min(nums1[1], nums2[1])))/2

def getMedian(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    l = len(nums)
    if l % 2 == 1:
        return nums[l/2]
    else:
        return (nums[l/2]+nums[l/2-1])/2

if __name__ == "__main__":
    nums1 = []
    nums2 = []
    for i in range(100):
        nums1.append(randint(0, 100))
        nums2.append(randint(0, 100))
    print Solution().findMedianSortedArrays(nums1, nums2)
    print getMedian(nums1, nums2)

