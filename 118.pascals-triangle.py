#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows: int) -> list[list[int]]:
        rows = []
        for i in range(numRows):
            if i == 0:
                rows.append([1])
                continue

            curr_row = []
            for j in range(i+1):
                left = rows[i-1][j-1] if j-1 >= 0 else 0
                right = rows[i-1][j] if j < len(rows[i-1]) else 0
                curr_row.append(left + right)
            rows.append(curr_row)
            
        return rows

# @lc code=end

