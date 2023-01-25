#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        def get_left_sum(node: TreeNode | None, is_left_node: bool) -> int:
            if node is None:
                return 0
            
            if node.left is None and node.right is None and is_left_node:
                return node.val

            return get_left_sum(node.left, True) + get_left_sum(node.right, False)
        return get_left_sum(root, False)
# @lc code=end

