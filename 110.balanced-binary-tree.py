#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        # returns depth and is_balanced
        def find_depth(node: TreeNode | None, current_depth: int) -> tuple[int, bool]:
            if node is None:
                return (current_depth, True)
            
            (left_depth, left_balanced) = find_depth(node.left, current_depth)
            (right_depth, right_balanced) = find_depth(node.right, current_depth)
            
            is_not_balanced = abs(left_depth - right_depth) > 1 or not left_balanced or not right_balanced
            depth = 1 + max(left_depth, right_depth)
            return (depth, not is_not_balanced)
        
        (_, is_balanced) = find_depth(root, 0)
        return is_balanced
        
# @lc code=end

