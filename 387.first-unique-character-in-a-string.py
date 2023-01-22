#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        def char_to_index(char: str) -> int:
            return ord(c) - 97 

        char_count = [0] * 26
        for c in s:
            char_count[char_to_index(c)] += 1
        
        for idx, c in enumerate(s):
            if char_count[char_to_index(c)] == 1:
                return idx
        
        return -1
# @lc code=end

