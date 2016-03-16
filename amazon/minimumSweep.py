'''
Minimum number of swaps required for arranging pairs adjacent to each other
There are n-pairs and therefore 2n people. everyone has one unique number ranging from 1 to 2n. All these 2n persons are
arranged in random fashion in an Array of size 2n. We are also given who is partner of whom. Find the minimum number of
swaps required to arrange these pairs such that all pairs become adjacent to each other.

Example:

Input:
n = 3  
pairs[] = {1->3, 2->6, 4->5}  // 1 is partner of 3 and so on
arr[] = {3, 5, 6, 4, 1, 2}

Output: 2
We can get {3, 1, 5, 4, 6, 2} by swapping 5 & 6, and 6 & 1

'''

def solution(pairs, nums):
    if not nums or len(nums) == 0:
        return 0
    assert (len(nums) % 2) == 0 

    map1 = {} # the neighbor map
    map2 = {} # the index map
    for i in range(len(nums)):
        map2[nums[i]] = i
    for item in pairs:
        map1[item[0]] = item[1]
        map1[item[1]] = item[0]
   
    return helper(0, nums, map1, map2)

def helper(i, nums, map1, map2):
    if i == len(nums):
    
        return 0
    
    l = nums[i]
    r = nums[i+1]
    lpair = map1[l]
    rpair = map1[r]
    if lpair == r and rpair == l:
        return helper(i+2, nums, map1, map2)
    else:
        mini = float('inf')
        swap(map2[lpair], i+1, nums)
        mini = min(mini, 1+helper(i+2, nums, map1, map2))
        swap(map2[lpair], i+1, nums)
        swap(map2[rpair], i, nums)
        mini = min(mini, 1+helper(i+2, nums, map1, map2))
        swap(map2[rpair], i, nums)
        return mini

def swap(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    print nums
            
pairs = [[1,2], [3,4], [5,6], [7,8]]    
nums  = [3,5,6,4,1,2, 8, 7]
print pairs
print solution(pairs, nums)
