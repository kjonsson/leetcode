#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        values = []
        def get_values(node: TreeNode | None):
            if node is not None:
                get_values(node.left)
                values.append(node.val)
                get_values(node.right)

        get_values(root)
        values.sort()

        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

        return int(min_diff)
# @lc code=end

