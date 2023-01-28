#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        sorted_nums = list(nums)
        sorted_nums.sort()
        return sorted_nums[-3]
# @lc code=end

