#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if bin(n).count('1') != 1:
            return False
        
        # Only single bit set and only in odd positions
        while n:
            if n & 2 > 0:
                return False
            n >>= 2
        
        return True
# @lc code=end