#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        head = ListNode(-1)
        curr = head
        while list1 is not None or list2 is not None:
            if not list1:
                curr.next = list2
                list2 = list2.next
            elif not list2:
                curr.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        return head.next
        
# @lc code=end

