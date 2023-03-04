#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []

        stack = [root.val]
        for child in root.children:
            stack += self.preorder(child)
        
        return stack
        
# @lc code=end

