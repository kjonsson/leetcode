#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ''
        
        result = ''
        for idx, chars_at_idx in enumerate(zip(*strs)):
            if len(set(chars_at_idx)) != 1:
                break
            
            result = strs[0][:idx+1]
            
        return result
        
# @lc code=end

s = Solution()
print(s.longestCommonPrefix(["cir","car"]))