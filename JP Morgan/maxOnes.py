class Solution:
    def rowWithMax1s(self, mat):
        m, n = len(mat), len(mat[0])
        best, i, j = -1, 0, n - 1
        while i < m and j >= 0:
            if mat[i][j] == 1:
                best = i
                j -= 1
            else:
                i += 1
        return best
