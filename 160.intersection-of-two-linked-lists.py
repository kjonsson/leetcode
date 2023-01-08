#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode | None = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        found_nodes = set()

        # Store values from a
        node_a = headA
        while node_a is not None:
            found_nodes.add(node_a)
            node_a = node_a.next
            
        # Find common node
        node_b = headB
        while node_b is not None:
            if node_b in found_nodes:
                return node_b
            node_b = node_b.next

        return None
# @lc code=end

