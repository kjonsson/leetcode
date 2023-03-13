#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        if root is None:
            return ""
        
        if root.left is not None and root.right is not None:
            return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
        
        if root.left is not None:
            return f"{root.val}({self.tree2str(root.left)})"
        
        if root.right is not None:
            return f"{root.val}()({self.tree2str(root.right)})"
        
        return f"{root.val}"
# @lc code=end

