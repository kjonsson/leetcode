#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        indexes = []
        vowels = 'aeiouAEIOU'
        for idx, val in enumerate(s):
            if val in vowels:
                indexes.append(idx)
                
        
        start = 0
        end = len(indexes) - 1
        while start < end:
            start_index = indexes[start]
            end_index = indexes[end]
            s[start_index], s[end_index] = s[end_index], s[start_index]
            start += 1
            end -= 1
            
        return ''.join(s)
# @lc code=end

