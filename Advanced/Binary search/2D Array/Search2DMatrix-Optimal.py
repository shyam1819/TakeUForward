class Solution:
    def searchMatrix(self, mat, target):
        m = len(mat)
        n = len(mat[0])
        high = (n*m)-1
        low = 0
        while low<=high:
            mid = (low+high)//2
            row = mid//n
            column = mid%n
            if mat[row][column]==target:
                return True
            elif mat[row][column]>target:
                high = mid-1
            else:
                low = mid+1
        return False
