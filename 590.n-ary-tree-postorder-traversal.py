#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        result = []

        def traverse(node):
            if node is None:
                return

            for child in node.children:
                traverse(child)

            result.append(node.val)

        traverse(root)
        return result

        
        
# @lc code=end

