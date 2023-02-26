#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode | None) -> int:
        result = 0

        def calculate_tilt(node: TreeNode | None) -> int:
            nonlocal result
            if node is None:
                return 0

            left = calculate_tilt(node.left)
            right = calculate_tilt(node.right)
            result += abs(left - right)

            return left + right + node.val
        
        calculate_tilt(root)
        return result
        
# @lc code=end

