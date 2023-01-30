#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 0
        curr = 0
        while curr < n:
            result += 1
            curr += result

        return result if curr == n else result - 1
        
# @lc code=end

