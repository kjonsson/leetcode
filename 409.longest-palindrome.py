#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import defaultdict
from typing import DefaultDict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter: DefaultDict[str, int] = defaultdict(int)
        for c in s:
            counter[c] += 1
            
        result = 0
        found_odd_number = False
        for c, _ in counter.items():
            result += counter[c] // 2 * 2
            found_odd_number = found_odd_number or counter[c] % 2 != 0
                
        return result + int(found_odd_number)
# @lc code=end

