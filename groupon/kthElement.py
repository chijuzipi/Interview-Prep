'''
find the kth smallest element from an array
followup: find the top k element

1) using quick sort as below
2) using bucket sort

'''

from random import randint
def kthElement(nums, k):
    if nums == None or k < 1:
        return None
    l = 0
    r = len(nums)-1
    while True:
        index = partition(nums ,l, r)
        if index == k-1:
            return nums[:index+1]
        elif index > k-1:
            r = index-1
        else:
            l = index+1


def partition(nums, l, r):
    if l == r:
        return l
    pivot = nums[r]
    slow  = l
    fast  = l
    while fast < r:
        if nums[fast] < pivot:
            swap(slow, fast, nums)
            slow += 1
        fast += 1
    swap(slow, r, nums)
    return slow

def swap(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

'''
nums = [0, 23, 26, 5, 20]
partition(nums,0, len(nums)-1)
print nums
'''
#for i in range(100):
nums = []
for i in range(100):
    nums.append(randint(0, 100))
a =  kthElement(nums, 50)
nums.sort()
b =  nums[:49+1]
a.sort()
print a
print b
