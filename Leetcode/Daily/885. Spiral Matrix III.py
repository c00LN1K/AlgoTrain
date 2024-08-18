from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        left_col = right_col = curr_col = cStart
        up_row = down_row = curr_row = rStart
        ans = []
        while len(ans) != rows * cols:
            while curr_col <= right_col:
                ans.append([curr_row, curr_col])
                curr_col += 1
            right_col = min(right_col + 1, cols)

            if right_col == cols:
                curr_col = cols - 1

            while curr_row <= down_row:
                ans.append([curr_row, curr_col])
                curr_row += 1
            down_row = min(down_row + 1, rows)

            while curr_col >= left_col:
                ans.append([curr_row, curr_col])
                curr_col -= 1
            left_col = max(left_col - 1, 0)

            while curr_row >= up_row:
                ans.append([curr_row, curr_col])
                curr_row -= 1
            up_row = max(up_row - 1, 0)

        return ans

print(Solution().spiralMatrixIII(5, 6, 1, 4))
