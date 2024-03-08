class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        rows = [1] * m
        cols = [1] * n
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    cols[j] = 0
                    rows[i] = 0

        i = max(m, n) - 1
        while i > -1:
            if m > i and not rows[i]:
                matrix[i] = [0] * n
            if n > i and not cols[i]:
                for j in range(m):
                    matrix[j][i] = 0
            i -= 1
        print(matrix)


print(Solution().setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]))
