#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        average_per_level = []

        if root is None:
            return average_per_level
        
        queue = [root]
        while queue:
            level_values = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average_per_level.append(sum(level_values) / len(level_values))

        return average_per_level


# @lc code=end

