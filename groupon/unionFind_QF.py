'''
Union Find: Quick Find method

'''
from random import randint
import time
class UnionFind(object):
    def __init__(self, n):
        self.item = [] 
        for i in range(n):
            self.item.append(i)
    
    # return True if two item are connected
    def find(self, i1, i2):
        return self.item[i1] == self.item[i2]
    
    # union two items
    def unite(self, i1, i2):
        id = self.item[i1]
        for i in range(len(self.item)):
            if self.item[i] == id:
                self.item[i] = self.item[i2]

def main():
    s1 = time.time()
    union = UnionFind(10000)
    for i in range(5000):
        i1 = randint(0, 9)
        i2 = randint(0, 9)
        union.unite(i1, i2)
    t1 = time.time()

    s2 = time.time()
    for i in range(5000):
        i1 = randint(0, 9)
        i2 = randint(0, 9)
        union.find(i1, i2)
    t2 = time.time()
    print 'union time: ', t1-s1
    print 'find time: ', t2-s2

if __name__ == "__main__":
    main()
        


         
