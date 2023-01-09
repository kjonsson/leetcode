#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
from string import ascii_uppercase

class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []
        
        while n > 0:
            remainder = (n-1) % 26
            n = (n-1) // 26

            char = ascii_uppercase[remainder]
            
            result = [char] + result
            
        return ''.join(result)

# @lc code=end

