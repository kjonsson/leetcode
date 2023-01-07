#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode | None = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next
        
        while slow is not None and fast is not None:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next
            
            if fast is not None:
                fast = fast.next
        
        return False
# @lc code=end

