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
        answer = 0

        def traverse(node: TreeNode | None) -> int:
            nonlocal answer

            if node is None:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            answer = max(answer, left + right)

            return max(left, right) + 1
        
        traverse(root)

        return answer
# @lc code=end

