class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        i = 0
        m = len(matrix[0])
        j = m-1
        while i<n and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False


# Staircase Search => O(N+M)
# More Suitable for square matrices.

# Binary Search => O(NlogM)
# Skewed matrices when N is much less than M.
