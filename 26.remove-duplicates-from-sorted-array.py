#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicate_idx = 0
        duplicate_count = 0
        for idx, num in enumerate(nums[1:]):
            if num == nums[duplicate_idx]:
                duplicate_count += 1
                continue

            nums[duplicate_idx + 1] = num
            duplicate_idx += 1
        
        return len(nums) - duplicate_count
# @lc code=end

s = Solution()
a = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(a))
print(a)