#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        fake_head = ListNode(0, head)
        node = fake_head
        
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                continue
            
            node = node.next
        
        return fake_head.next
# @lc code=end

