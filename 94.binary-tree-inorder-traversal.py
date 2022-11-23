#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root == None:
            return []

        def in_order(node: TreeNode | None) -> list[int]:
            if node is None:
                return []
            
            result = []
            if node.left is not None:
                result = in_order(node.left)
            
            result = result + [node.val]
            
            if node.right is not None:
                result = result + in_order(node.right)
                
            return result
        
        result = in_order(root)
        print(result)
        
        return result 
            
# @lc code=end

