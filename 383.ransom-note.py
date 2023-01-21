#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        
        for char in magazine:
            counter[char] += 1
            
        for char in ransomNote:
            counter[char] -= 1
            
        return all([val >= 0 for val in counter.values()])        
# @lc code=end

