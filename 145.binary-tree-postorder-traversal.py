#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def traverse(node: TreeNode | None) -> None:
            if node is None:
                return

            traverse(node.left)
            traverse(node.right)

            result.append(node.val)

        traverse(root)
        return result

# @lc code=end

