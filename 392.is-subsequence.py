#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        s_idx = 0
        for val in t:
            if s_idx >= len(s):
                break

            if s[s_idx] == val:
                s_idx += 1
                
        return s_idx == len(s)
# @lc code=end

