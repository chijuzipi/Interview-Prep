class Solution(object):
    def numIslands2(self, m, n, positions):
        root1 = []
        root2 = []
        matrix = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            root1.append(i)
        for j in range(n):
            root2.append(j)
       
        num = 0
        out = []
        for pos in positions:
            i = pos[0]
            j = pos[1]
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                num += 1
                if i-1 >= 0 and matrix[i-1][j] == 1:
                    unite(root1, root2, i, j, i-1, j) 
                    num -= 1
                if j-1 >= 0 and matrix[i][j-1] == 1 and not find(root1, root2, i, j, i, j-1):
                    unite(root1, root2, i, j, i, j-1)
                    num -= 1
                if i+1 < m and matrix[i+1][j] == 1 and not find(root1, root2, i, j, i+1, j):
                    unite(root1, root2, i, j, i+1, j)
                    num -= 1
                if j+1 < n and matrix[i][j+1] == 1 and not find(root1, root2, i, j, i, j+1):
                    unite(root1, root2, i, j, i, j+1)
                    num -= 1
            out.append(num)
        return out

def find(root1, root2, i, j, k, l):
    return getRoot(root1, i) == getRoot(root1, k) and getRoot(root2, j) == getRoot(root2, l)

def getRoot(root, i):
    while i != root[i]:
        i = root[i]
    return i

def unite(root1, root2, i, j, k, l):

    
def main():
    m = 3
    n = 3
    positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
    print Solution().numIslands2(m, n, positions)
    # answer : [1,2,3,4,3,2,1]

if __name__ == "__main__":
    main()
"""
:type m: int
:type n: int
:type positions: List[List[int]]
:rtype: List[int]
"""
