#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root: TreeNode | None):
        if root is None:
            return None
        
        # Store left and right child nodes for later
        left_node = root.left
        right_node = root.right
        
        # Recursively flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Remove left subtree and replace right subtree with left subtree
        root.left = None
        root.right = left_node
        
        # Find last node that needs connecting to previous right subtree
        curr = root
        while curr.right is not None:
            curr = curr.right
        curr.right = right_node
        
        return root
        
# @lc code=end

