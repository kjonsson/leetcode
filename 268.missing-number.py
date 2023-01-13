#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum_of_all = (len(nums) * (len(nums) + 1)) / 2
        sum_found = sum(nums)
        return int(sum_of_all - sum_found)
# @lc code=end

