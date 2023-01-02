#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, target: int) -> bool:
        def check_path(node: TreeNode | None, curr_sum: int, target: int):
            if not node:
                return False
            
            curr_sum += node.val
            
            is_leaf = node.left is None and node.right is None
            
            if is_leaf:
                return curr_sum == target
            
            return (
                check_path(node.left, curr_sum, target) or
                check_path(node.right, curr_sum, target)
            )
        
        return check_path(root, 0, target)

# @lc code=end

