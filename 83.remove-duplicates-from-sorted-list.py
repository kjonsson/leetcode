#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        
        temp_head = ListNode(None, head)
        temp = temp_head
        
        while temp is not None and temp.next is not None:
            curr_val = temp.val
            next_val = temp.next.val
            if curr_val == next_val:
                temp.next = temp.next.next
                continue
            
            temp = temp.next
            
    
        return temp_head.next
# @lc code=end

