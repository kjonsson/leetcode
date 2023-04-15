#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        expected_numbers = list(range(1, len(nums) + 1))

        missing_number = list(set(expected_numbers) - set(nums))[0]

        return [sum(nums) - sum(set(nums)), missing_number]


        
# @lc code=end

