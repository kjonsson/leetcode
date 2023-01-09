#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        reversed_title = list(reversed(columnTitle))

        result = 0
        position = 1
        for char in reversed_title:
            number = ord(char) - 64
            result += number * position
            position *= 26
            
        return result
# @lc code=end

