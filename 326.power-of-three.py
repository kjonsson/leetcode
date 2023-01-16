#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        result = 1
        while result <= n:
            if result == n:
                return True
            result *= 3
                
        return False
# @lc code=end

