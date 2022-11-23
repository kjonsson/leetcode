#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        len1 = m
        len2 = n

        # Start from back of nums1 and fill in backwards
        nums1_backidx = len1 - 1
        nums2_backidx = len2 - 1
        result_backidx = len1 + len2 - 1

        while result_backidx >= 0:
            if nums1_backidx < 0:
                nums1[result_backidx] = nums2[nums2_backidx]
                nums2_backidx -= 1
                result_backidx -= 1
                continue
            elif nums2_backidx < 0:
                nums1[result_backidx] = nums1[nums1_backidx]
                nums1_backidx -= 1
                result_backidx -= 1
                continue
            


            num1 = nums1[nums1_backidx]
            num2 = nums2[nums2_backidx]
            
            if num1 > num2:
                nums1_backidx -= 1
            else:
                nums2_backidx -= 1
            
            nums1[result_backidx] = max(num1, num2)
            result_backidx -= 1
        return nums1
        
# @lc code=end

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))