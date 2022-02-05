from typing import *

# 817. Linked List Components
# https://leetcode.com/problems/linked-list-components/

# You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

# Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

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
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        components = set(nums)
        pointer = head.next
        prev = head
        counter = 0
        
        while(pointer):
            if(pointer.val not in components):
                if (prev.val in components):
                    counter += 1
            prev = pointer
            pointer = pointer.next
            
        if (prev.val in components):
            counter += 1
            
        return counter