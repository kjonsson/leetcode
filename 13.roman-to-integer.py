#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        for prev_char, curr_char in zip(s[:-1], s[1:]):
            prev_value = values[prev_char]
            current_value = values[curr_char]
            result += prev_value if prev_value >= current_value else -prev_value
            
        return result + values[s[-1]]
# @lc code=end

