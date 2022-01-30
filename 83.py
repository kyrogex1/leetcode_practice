from typing import *

# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pointer = head
        while (pointer is not None):
            if (prev is not None and prev.val == pointer.val):
                prev.next = pointer.next
            else:
                prev = pointer
            pointer = pointer.next
            
        return head
    
x = ListNode(1)
x.next = ListNode(3)
x.next.next = ListNode(3)
x.next.next.next = ListNode(3)
x.next.next.next.next = ListNode(7)
x.next.next.next.next.next = ListNode(7)
x.next.next.next.next.next.next = ListNode(7)

print(Solution().deleteDuplicates(x))