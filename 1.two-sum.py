#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        val_to_idx = {}            
        for idx, val in enumerate(nums):
            val_to_find = target - val
            
            if val_to_find in val_to_idx:
                return [val_to_idx[val_to_find], idx]
            
            val_to_idx[val] = idx
            
        
# @lc code=end

