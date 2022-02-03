from typing import *

# 86. Partition List
# https://leetcode.com/problems/partition-list/

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)
        
class Solution:
    # Main idea is to traverse the LL, and then build up 2 linked lists
    # 1. LL1, LL for values less than x
    # 2. LL2, LL for values greater than or equal x
    # Then set the head to the start of LL1
    # Connect tail of LL1 to LL2
    # Set the tail of LL2 to point to None to end the LL
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesserPointer = greaterPointer = None
        lesserStartingPoint = greaterStartingPoint = None
        pointer = head
        
        while(pointer is not None):
            if (pointer.val < x):
                if (lesserStartingPoint is None):
                    lesserStartingPoint = pointer
                    # Yes we can actually just set head here instead of using an extra pointer to keep track of lesserStartingPoint. But I think this is more readable
                else:
                    lesserPointer.next = pointer
                lesserPointer = pointer
            else:
                if (greaterStartingPoint is None):
                    greaterStartingPoint = pointer
                else:
                    greaterPointer.next = pointer
                greaterPointer = pointer
            pointer = pointer.next
        
        # If there are no values less than x, ie LL1 is empty, just return head
        if (lesserStartingPoint is None):
            return head
        # Else we set the tail of LL1 to point to the LL2
        # Also set the head to point to LL1
        else:
            head = lesserStartingPoint
            lesserPointer.next = greaterStartingPoint
            
        # Set the tail of greaterPointer to None to end the LL
        if (greaterStartingPoint is not None):
            greaterPointer.next = None
            
        return head
    
# x = ListNode(1)
# x.next = ListNode(1)
# x.next.next = ListNode(7)
# x.next.next.next = ListNode(3)
# x.next.next.next.next = ListNode(2)
# x.next.next.next.next.next = ListNode(3)

# print(Solution().partition(x, 7))
