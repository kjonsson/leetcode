#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = [-1] * len(nums1)

        for index1, num1 in enumerate(nums1):
            val_found = False

            for index2, num2 in enumerate(nums2):
                if num2 == num1:
                    val_found = True
                    continue

                if not val_found:
                    continue

                if val_found and num2 > num1 and result[index1] == -1:
                    result[index1] = num2

        return result
# @lc code=end


