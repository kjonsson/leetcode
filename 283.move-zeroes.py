#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        length = len(nums)
        swap_idx = 0
        for idx in range(length):
            if nums[idx] == 0:
                continue
            
            nums[swap_idx], nums[idx] = nums[idx], nums[swap_idx]
            swap_idx += 1
        
# @lc code=end

