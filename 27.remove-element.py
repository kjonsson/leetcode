#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        curr_idx = 0
        for num in nums:
            if num == val:
                continue

            nums[curr_idx] = num
            curr_idx += 1
                
        return curr_idx
# @lc code=end