#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for i in range(32):
            counter += n & 1
            n >>= 1
        return counter
# @lc code=end

