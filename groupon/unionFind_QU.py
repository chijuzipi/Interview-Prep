'''
Union Union: Quick Union method

'''
from random import randint
import time
class UnionFind(object):
    def __init__(self, n):
        self.item = [] 
        self.sz = [1] * n
        for i in range(n):
            self.item.append(i)
    
    # return True if two item are connected
    def find(self, i1, i2):
        return self.root(i1) == self.root(i2)

    def root(self, i):
        while self.item[i] != i:
            self.item[i] = self.item[self.item[i]]
            i = self.item[i]
        return i
    
    # union two items
    def unite(self, i1, i2):
            
        root1 = self.root(i1)
        root2 = self.root(i2)
        if self.sz[i1] < self.sz[i2]:
            self.item[root1] = root2
            self.sz[i2] += self.sz[i1]
        else:
            self.item[root2] = root1
            self.sz[i1] += self.sz[i2]


def main():
    s1 = time.time()
    union = UnionFind(10000000)
    for i in range(200000):
        i1 = randint(0, 9)
        i2 = randint(0, 9)
        union.unite(i1, i2)
    t1 = time.time()

    s2 = time.time()
    for i in range(200000):
        i1 = randint(0, 9)
        i2 = randint(0, 9)
        union.find(i1, i2)
    t2 = time.time()
    print 'union time: ', t1-s1
    print 'find time: ', t2-s2

if __name__ == "__main__":
    main()
        


         
