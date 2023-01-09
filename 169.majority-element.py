#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        target = len(nums) // 2
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
            if counter[num] > target:
                return num
# @lc code=end

