#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.


from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        count: defaultdict[int, int] = defaultdict(int)

        def traverse(node: TreeNode | None):
            if node is None:
                return

            count[node.val] = count.get(node.val, 0) + 1
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        max_count = max(count.values())

        return [k for k, v in count.items() if v == max_count]
# @lc code=end

