class Solution:
    def pascalTriangleII(self, r):
        row = [0]*r
        n = r//2 if r%2==0 else (r//2)+1
        row[0] = 1
        for i in range(0,n):
            if i!=0:
                row[i] = row[i-1]*(r-i)//i
            row[r-i-1] = row[i]
        return row
