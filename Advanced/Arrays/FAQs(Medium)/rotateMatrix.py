class Solution:
    def rotateMatrix(self, matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(N):
            matrix[i].reverse()
