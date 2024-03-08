class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        s = set()
        s.add((0, 0))
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        ans = [matrix[0][0]]
        while len(s) != (m * n):
            while 0 <= (j + 1) < n and (i, j + 1) not in s:
                j += 1
                s.add((i, j))
                ans.append(matrix[i][j])
            while 0 <= (i + 1) < m and (i + 1, j) not in s:
                i += 1
                s.add((i, j))
                ans.append(matrix[i][j])
            while 0 <= (j - 1) < n and (i, j - 1) not in s:
                j -= 1
                s.add((i, j))
                ans.append(matrix[i][j])
            while 0 <= (i - 1) < m and (i - 1, j) not in s:
                i -= 1
                s.add((i, j))
                ans.append(matrix[i][j])
        return ans


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
