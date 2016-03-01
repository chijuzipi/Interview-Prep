'''
Median in a stream of integers (running integers)
Given that integers are read from a data stream. Find median of elements read so for in efficient way. For simplicity
assume there are no duplicates. For example, let us consider the stream 5, 15, 1, 3 …

After reading 1st element of stream - 5 -> median - 5
After reading 2nd element of stream - 5, 15 -> median - 10
After reading 3rd element of stream - 5, 15, 1 -> median - 5
After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

'''
from heapq import heappush, heappop
def findMedian(nums):
    minH = MinHeap()
    maxH = MaxHeap()

    for i in range(len(nums)):
        here = nums[i]
        res  = 0
        if len(minH.q) == len(maxH.q):
            mini = minH.peek() 
            maxi = maxH.peek()
            res = (mini+maxi)/2
            if here > mini:
                minH.push(here)
            else:
                maxH.push(here)

        if len(minH.q) != len(maxH.q):
            if len(minH.q) > len(maxH.q):
                res = minH.peek()
                maxH.push(here)
            else:
                res = maxH.peek()
                minH.push(here)

            mini = minH.peek()
            maxi = maxH.peed()
            if mini < maxi:
                minH.pop()
                maxH.pop()
                minH.push(maxi)
                maxH.push(mini)
        print res

object MinHeap(object):
    def __init__(self):
        self.q = []
    
    def push(self, x):
        heappush(self.q, x) 

    def pop(self):
        return heappop(self.q)

    def peek(self):
        return self.q[0]

object MaxHeap(object):
    def __init__(self):
        self.q = []
    
    def push(self, x):
        heappush(self.q, -x) 

    def pop(self):
        return -1 * heappop(self.q)

    def peek(self):
        return -1 * self.q[0]

