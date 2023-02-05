#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        zeros_and_ones = str(bin(num))[2:]
        return int(''.join(['1' if x == '0' else '0' for x in zeros_and_ones]), 2)
# @lc code=end

