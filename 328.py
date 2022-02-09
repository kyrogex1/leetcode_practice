from typing import *

# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    def printLL(self):
        pointer = self
        while(pointer is not None):
            print(pointer.val, end = ' ')
            pointer = pointer.next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head
        
        isOdd = True
        pointer = head
        prevOdd = None
        prevEven = None
        firstEven = None
        
        while (pointer):
            if (isOdd):
                if (prevOdd):
                    prevOdd.next = pointer
                prevOdd = pointer
            else:
                if (prevEven):
                    prevEven.next = pointer
                if (firstEven is None):
                    firstEven = pointer
                prevEven = pointer
            pointer = pointer.next
            isOdd = not isOdd
            
        prevOdd.next = firstEven
        prevEven.next = None
        
        return head