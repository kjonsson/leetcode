#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None:
            return True
        
        values = []

        node = head
        while node is not None:
            values.append(node.val)
            node = node.next

        return values == values[::-1]
# @lc code=end

