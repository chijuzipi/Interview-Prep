'''
'''
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.root = []
        self.row  = m
        self.col  = n
        self.size = []
        matrix = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                index = self.getIndex(i, j)
                self.root.append(index)
                self.size.append(1)
        out = []
        num = 0
        for pos in positions:
            i = pos[0]
            j = pos[1]
            index = self.getIndex(i, j)
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                num += 1
                if i-1 >= 0 and matrix[i-1][j] == 1:
                    upindex = self.getIndex(i-1, j)
                    if not self.find(index, upindex):
                        self.unite(index, upindex)
                        num -= 1
                if j-1 >= 0 and matrix[i][j-1] == 1:
                    leftindex = self.getIndex(i, j-1)
                    if not self.find(index, leftindex):
                        self.unite(index, leftindex)
                        num -= 1
                if i+1 < m and matrix[i+1][j] == 1:
                    downindex = self.getIndex(i+1, j)
                    if not self.find(index, downindex):
                        self.unite(index, downindex)
                        num -= 1
                if j+1 < n and matrix[i][j+1] == 1:
                    rightindex= self.getIndex(i, j+1)
                    if not self.find(index, rightindex):
                        self.unite(index, rightindex)
                        num -= 1
            out.append(num)
        return out
        
    def getIndex(self, i, j):
        return self.col * i + j
        
    def unite(self, i, j):
        p = self.getRoot(i)
        q = self.getRoot(j)
        if self.size[p] > self.size[q]:
            self.root[q] = p
            self.size[p] += self.size[q]
        else:
            self.root[p] = q
            self.size[q] += self.size[p]
    
    def find(self, i, j):
        p = self.getRoot(i)
        q = self.getRoot(j)
        return q == p
        
    def getRoot(self, i):
        #print i, len(self.root)
        while self.root[i] != i:
            self.root[i] = self.root[self.root[i]]
            i = self.root[i]
        return i


m = 8
n = 4
pos = [[0,0],[7,1],[6,1],[3,3],[4,1]]
print Solution().numIslands2(m, n, pos)
