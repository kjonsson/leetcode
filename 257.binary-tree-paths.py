#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if root is None:
            return []
        
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        
        if not left_paths and not right_paths:
            return [str(root.val)]
        
        result = []
        for path_ in left_paths:
            result.append(f'{root.val}->{path_}')
            
        for path_ in right_paths:
            result.append(f'{root.val}->{path_}')
            
        return result
# @lc code=end

