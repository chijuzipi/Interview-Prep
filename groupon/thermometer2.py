'''
Design an algorithm for a thermometer that shows the Maximum and minimum temperature in the last 24 hours.  The current
temperature can be read in 5 second intervals.

--> two linkedlist
--> when getMin, remove expired element from the head
--> when insert, remove bigger (since they are also older) element from the tail
'''
from collections import deque
class Thermoter(object):
    def __init__(self):
        self.miniList = deque()
        self.maxiList = deque()

    def read(self, x, time):
        while len(self.miniList) > 0 and x <= self.miniList[-1][0]:
            self.miniList.pop()
        self.miniList.append((x, time))

        while len(self.maxiList) > 0 and x >= self.maxiList[-1][0]:
            self.maxiList.pop()
        self.maxiList.append((x, time))

     
    def getMin(self, time):
        while len(self.miniList) > 0 and time - self.miniList[0][1] > 3: # set 3 as the time frame for expiration
            self.miniList.popleft()
        mini = self.miniList[0][0]
        return mini

    def getMax(self, time):
        while len(self.maxiList) > 0 and time - self.maxiList[0][1] > 3:
            self.maxiList.popleft()
        maxi = self.maxiList[0][0]
        return maxi

the = Thermoter()
the.read(25, 1)
the.read(24, 2)
the.read(27, 3)
the.read(22, 4)
the.read(26, 5)
the.read(20, 6)
the.read(19, 7)
print the.miniList
print the.maxiList
print the.getMin(7)
print the.getMax(7)
print the.miniList
print the.maxiList
        
