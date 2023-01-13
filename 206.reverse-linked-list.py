#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        
        fake_head = ListNode(-1, head)

        prev_node = fake_head
        curr_node: ListNode | None = head
        next_node = head.next
        
        while curr_node is not None:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

            if next_node is not None:
                next_node = next_node.next
            
        
        if fake_head.next is not None:
            fake_head.next.next = None

        return prev_node
# @lc code=end

