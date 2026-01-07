class Solution:
    def spiralOrder(self, matrix):
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        arr = []

        while top <= bottom and left <= right:
            for i in range(left,right+1):
                arr.append(matrix[top][i])
            top+=1
            for i in range(top,bottom):
                arr.append(matrix[i][right])
            if top<=bottom:
                for i in range(right,left-1,-1):
                    arr.append(matrix[bottom][i])
                right-=1
                bottom-=1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    arr.append(matrix[i][left])
                left+=1
        return arr
