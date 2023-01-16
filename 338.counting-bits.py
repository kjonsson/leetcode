#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, total: int) -> list[int]:
        result = []
        for num in range(total + 1):
            curr_result = 0

            while num > 0:
                curr_result += num & 1
                num = num >> 1
            
            result.append(curr_result)

        return result
# @lc code=end

