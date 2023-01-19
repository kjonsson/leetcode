#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from collections import defaultdict


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        found_number_counts = defaultdict(int)
        for n in nums1:
            found_number_counts[n] += 1
            
        for n in nums2:
            if found_number_counts[n] > 0:
                result.append(n)
                found_number_counts[n] -= 1
                
        return result
# @lc code=end

