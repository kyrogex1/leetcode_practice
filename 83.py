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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headAssigned = False
        while (True):
            if (not headAssigned):
                head = self.findNextValidNumber(head, ListNode(9999))
                headAssigned = True
                if (head is None):
                    return head
                else:
                    pointer = head
            else:
                pointer.next = self.findNextValidNumber(pointer.next, pointer)
                if (pointer.next is None):
                    break
                pointer = pointer.next

        return head

    def findNextValidNumber(self, head, prev):
        pointer = head
        isCandidateValid = False

        while(pointer is not None):
            if (pointer.val != prev.val):
                if (isCandidateValid):
                    break
                else:
                    isCandidateValid = True
            else:
                isCandidateValid = False
            prev = pointer
            pointer = pointer.next

        if (isCandidateValid):
            result = prev
        else:
            result = None

        return result

    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if (head is None):
    #         return head

    #     pointer = head
    #     currentValIsValid = True
    #     while(pointer.next is not None):
    #         if (pointer.next.val == pointer.val):
    #             currentValIsValid = False
    #         else:
    #             if (currentValIsValid):
    #                 break
    #             else:
    #                 currentValIsValid = True
    #         pointer = pointer.next

    #     if (pointer.next is not None):
    #         head = pointer
    #     else:
    #         return None

        


# x = ListNode(1)
# x.next = ListNode(3)
# x.next.next = ListNode(3)
# x.next.next.next = ListNode(3)
# x.next.next.next.next = ListNode(7)
# x.next.next.next.next.next = ListNode(8)
# x.next.next.next.next.next.next = ListNode(8)
# x.next.next.next.next.next.next.next = ListNode(9)
# x.next.next.next.next.next.next.next.next = ListNode(10)

x = ListNode(1)
x.next = ListNode(1)
x.next.next = ListNode(1)
x.next.next.next = ListNode(2)
x.next.next.next.next = ListNode(3)
print(Solution().deleteDuplicates(x))