#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode:
        if root is None:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right, root.left = left, right
        
        return root
            
# @lc code=end

