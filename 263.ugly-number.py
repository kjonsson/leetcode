#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 0:
            if num % 5 == 0:
                num //= 5
                continue
            if num % 3 == 0:
                num //= 3
                continue
            if num % 2 == 0:
                num //= 2
                continue
            
            break
            
        return num == 1
# @lc code=end

