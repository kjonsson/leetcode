#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binary_search(start: int, end: int) -> int:
            if start >= end:
                return start
            
            middle = start + ((end - start) // 2)
            
            is_bad = isBadVersion(middle)
            
            if is_bad:
                end  = middle
            else:
                start = middle + 1
                
            return binary_search(start, end)
        
        return binary_search(1, n)
# @lc code=end

