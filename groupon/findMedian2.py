'''
find median of two array with the same length
'''
from random import randint
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1+l2) % 2 == 0:
            r1 = find(nums1, 0, l1, nums2, 0, l2, (l1+l2)/2)
            r2 = find(nums1, 0, l1, nums2, 0, l2, (l1+l2)/2 + 1)
            return (r1 + r2)/2.0
        else:
            return find(nums1, 0, l1, nums2, 0, l2, (l1+l2+1)/2)


def find(A, sa, ta, B, sb, tb, k):
    la = ta-sa
    lb = tb-sb
    if la <= 0:
        return B[sb+k-1]
    if lb <= 0:
        return A[sa+k-1]
    if k == 1:
        return A[sa] if A[sa] < B[sb] else B[sb]

    midA = (sa+ta)/2
    midB = (sb+tb)/2
    if A[midA] <= B[midB]:
        if la/2 + lb/2 + 1 >= k:
            return find(A, sa, ta, B, sb, midB, k)
        else:
            return find(A, midA + 1, ta, B, sb, tb, k-la/2-1)
    else:
        if la/2 + lb/2 + 1 >= k:
            return find(A, sa, midA, B, sb, tb, k)
        else:
            return find(A, sa, ta, B, midB+1, tb, k-lb/2-1)


def getMedian(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    print nums1
    print nums2
    print nums
    l = len(nums)
    if l % 2 == 1:
        return nums[l/2]
    else:
        return float((nums[l/2]+nums[l/2-1])/2.0)

if __name__ == "__main__":
    nums1 = []
    nums2 = []
    for i in range(5):
        nums1.append(randint(0, 100))
        nums2.append(randint(0, 100))
    nums1.sort()
    nums2.sort()
    print Solution().findMedianSortedArrays(nums1, nums2)
    print getMedian(nums1, nums2)
            
        
