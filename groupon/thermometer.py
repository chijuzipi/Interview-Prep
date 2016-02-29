'''
Design an algorithm for a thermometer that shows the Maximum and minimum temperature in the last 24 hours.  The current
temperature can be read in 5 second intervals.

--> two linkedlist
--> when getMin, remove expired element from the head
--> when insert, remove bigger (since they are also older) element from the tail

'''

class Thermoter(object):
    def __init__(self, nums, k):
        self.max = Node(None, None)
        self.min = Node(None, None)
    
    def read(self, x):
        self.insert(x) 

    def getMin(self):
        curr = self.min.next
        while curr and expire(curr.time):
            temp = curr.next
            remove(curr)
            curr = temp
        return self.min.next

    def getMax(self):
        curr = self.min.next
        while curr and expire(curr.time):
            temp = curr.next
            remove(curr)
            curr = temp
        return self.min.next


    def insert(self, x):
        tail = self.tail
        while tail < x

def expire

class Node(object):
    def __init__(self, temp, time):
        self.temp = temp
        self.time = time
        self.next = None
        self.prev = None
        

