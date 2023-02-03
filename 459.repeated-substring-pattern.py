#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            substring = s[:i+1]
            if len(s) % len(substring) != 0:
                continue

            if substring * (len(s) // len(substring)) == s:
                return True

        return False
# @lc code=end

