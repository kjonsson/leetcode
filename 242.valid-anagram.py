#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        
        for val in s:
            counter[val] += 1
            
        for val in t:
            counter[val] -= 1
            
        for val in counter.values():
            if val != 0:
                return False
            
        return True
# @lc code=end

