'''
There are given n ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two
ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.

For example if we are given 4 ropes of lengths 4, 3, 2 and 6. We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all ropes have connected.

Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. Other ways of
connecting ropes would always have same or more cost. For example, if we connect 4 and 6 first (we get three strings of
3, 2 and 10), then connect 10 and 3 (we get two strings of 13 and 2). Finally we connect 13 and 2. Total cost in this
way is 10 + 13 + 15 = 38.

'''

'''
--> corner case:
1) ropes == None or len(ropes) == 0 or len(ropes) == 1
2) ropes[i] < 0?

--> time: O(n), space: O(n)
'''

from heapq import heappush, heappop

class Solution(object):
    def join(self, ropes):
        if ropes == None or len(ropes) == 0 or len(ropes) == 1:
            return 0

        q = []
        for i in ropes:
            heappush(q, i)

        cost = 0
        while len(q) > 1:
            l1 = heappop(q)
            l2 = heappop(q)
            cost += l1 + l2
            heappush(q, l1 + l2)
        return cost

if __name__ == "__main__":
    ropes = [4,3,2,6,5, 12, 6, 7]
    print Solution().join(ropes)
