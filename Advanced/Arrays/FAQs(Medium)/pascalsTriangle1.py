class Solution:
    def pascalTriangleI(self, r, c):
        return self.combination(r-1,c-1)
        
    def combination(self,n,r):
        if r > n-r:
            r = n-r
        if r == 1:
            return n
        prod = 1
        for i in range(r):
            prod*=(n-i)
            prod/=(i+1)
        return int(prod)
