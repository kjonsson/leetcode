#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def is_same_tree(node1: TreeNode | None, node2: TreeNode | None) -> bool:
            if node1 is None and node2 is None:
                return True

            if node1 is None:
                return False
            
            if node2 is None:
                return False

            if node1.val != node2.val:
                return False

            return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)
        
        if root is None:
            return False
        
        if is_same_tree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
# @lc code=end

