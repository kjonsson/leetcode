#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int | None = None, children: list['Node'] | None = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:

        def calculate_max_depth(node: Node | None, depth: int) -> int:
            if node is None:
                return depth

            if node.children is None:
                return depth + 1

            if len(node.children) == 0:
                return depth + 1

            return max(calculate_max_depth(child, depth + 1) for child in node.children)

        return calculate_max_depth(root, 0)
        
# @lc code=end

