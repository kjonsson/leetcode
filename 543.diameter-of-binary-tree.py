#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        longest_diameter = 0

        def calculate_depth(node: TreeNode | None) -> int:
            nonlocal longest_diameter

            if node is None:
                return 0

            left = calculate_depth(node.left)
            right = calculate_depth(node.right)

            longest_diameter = max(longest_diameter, left + right)

            return max(left, right) + 1
        
        calculate_depth(root)

        return longest_diameter
# @lc code=end

