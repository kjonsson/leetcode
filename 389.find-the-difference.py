#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = defaultdict(int)

        for c in t: 
            counter[c] += 1

        for c in s:
            counter[c] -= 1

        for char, count in counter.items():
            if count == 1:
                return char

        raise ValueError('Weird, should have found value')
# @lc code=end

