#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        abs_num = abs(num)

        result = ''
        while abs_num > 0:
            result = str(abs_num % 7) + result
            abs_num //= 7
        
        if num < 0:
            result = '-' + result

        return result
# @lc code=end

