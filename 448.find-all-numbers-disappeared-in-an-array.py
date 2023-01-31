#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        found_numbers = set(nums)
        for num in nums:
            found_numbers.add(num)

        return [num for num in range(1, len(nums) + 1) if num not in found_numbers]


# @lc code=end
