#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if len(ops) == 0:
            return m * n

        row, col = ops[0]

        for op in ops[1:]:
            row = min(row, op[0])
            col = min(col, op[1])

        return row * col
# @lc code=end

