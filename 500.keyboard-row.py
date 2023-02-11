#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        result = []

        for word in words:
            word_lower = set(word.lower())

            if word_lower.issubset(row1) or word_lower.issubset(row2) or word_lower.issubset(row3):
                result.append(''.join(word))

        return result             
# @lc code=end

