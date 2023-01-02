#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def min_depth(node: TreeNode | None):
            if not node:
                return 0

            left = 0
            right = 0

            if node.left:
                left = self.minDepth(node.left)

            if node.right:
                right = self.minDepth(node.right)


            return 1 + min(left, right) if left > 0 and right > 0 else 1 + left + right
        
        return min_depth(root)

# @lc code=end

