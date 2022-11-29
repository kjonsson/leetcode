#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.bst(nums, 0, len(nums) - 1)
    
    def bst(self, nums: list[int], start: int, end: int) -> TreeNode | None:
        if start > end:
            return None
        
        idx = (start + end) // 2
        
        return TreeNode(
            val=nums[idx],
            left=self.bst(nums, start, idx - 1),
            right=self.bst(nums, idx + 1, end),
        )
# @lc code=end

