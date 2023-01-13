#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        result = num
        while result >= 10:
            result = sum([int(n) for n in list(str(result))])

        return result        
# @lc code=end

