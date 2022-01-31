from typing import *

# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)
        
class Solution:
    # The discussion section has a better solution. Its the Same Idea, but their traversal is better
    # Eg see how I have (if conditions for numberOfRotations == 0)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pointer = head

        # Find the length of LL
        length = 0
        while (pointer is not None):
            length += 1
            if (pointer.next is None):
                tail = pointer
            pointer = pointer.next

        if (length < 2):
            return head
            
        numberOfRotations = k % length
        newTailIndex = length - numberOfRotations
        pointer = head

        if (numberOfRotations == 0):
            return head
        
        # Traverse until we reach the node which needs to be moved to the head
        while (newTailIndex > 0):
            next = pointer.next
            newTailIndex -= 1
            # Set the new tail's next to None to end the LL
            if (newTailIndex == 0):
                pointer.next = None
            pointer = next
            
        tail.next = head
        head = pointer
        
        return head
    
x = ListNode(1)
x.next = ListNode(2)
# x.next.next = ListNode(3)
# x.next.next.next = ListNode(4)
# x.next.next.next.next = ListNode(5)
# x.next.next.next.next.next = ListNode(6)
# x.next.next.next.next.next.next = ListNode(7)

print(Solution().rotateRight(x, 2).val)