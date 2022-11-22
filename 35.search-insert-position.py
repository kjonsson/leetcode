#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[0] > target:
            return 0
        
        if nums[-1] < target:
            return len(nums)
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end-start) // 2)
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return max(start, mid)
# @lc code=end

