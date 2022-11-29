#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:    
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        def check_nodes(node1: TreeNode  | None, node2: TreeNode  | None) -> bool:
            if node1 is not None and node2 is None:
                return False
            
            if node2 is not None and node1 is None:
                return False
            
            if node1 is None and node2 is None:
                return True
            
            if node1.val != node2.val:
                return False
            
            
            return check_nodes(node1.left, node2.right) and check_nodes(node1.right, node2.left)
        
        return check_nodes(root, root)
        
# @lc code=end