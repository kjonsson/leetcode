#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s = {}
        s_to_pattern = {}

        string_arr = s.split(' ')

        if len(pattern) != len(string_arr):
            return False

        for idx, val in enumerate(s.split(' ')):
            pattern_at_idx = pattern[idx]

            if val in s_to_pattern and s_to_pattern[val] != pattern_at_idx:
                return False

            if pattern_at_idx in pattern_to_s and pattern_to_s[pattern_at_idx] != val:
                return False

            s_to_pattern[val] = pattern_at_idx
            pattern_to_s[pattern_at_idx] = val

        return True
# @lc code=end

