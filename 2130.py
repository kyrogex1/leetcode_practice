from typing import *

# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

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
    def pairSum(self, head: Optional[ListNode]) -> int:
        midPoint = self.midPoint(head)
        midPointReversedHead = self.reverse(midPoint)
        
        pointer = head
        maximumSum = 2 # Minimum is 2 based on question constraints
        while(midPointReversedHead is not None):
            addition = pointer.val + midPointReversedHead.val
            maximumSum = max(maximumSum, addition)
            midPointReversedHead = midPointReversedHead.next
            pointer = pointer.next
            
        return maximumSum
        
    def midPoint(self, head: Optional[ListNode]) -> int:
        tortoise = hare = head
        while(hare and hare.next):
            tortoise = tortoise.next
            hare = hare.next.next
            
        return tortoise
    
    def reverse(self, head: Optional[ListNode]) -> int:
        prev = None
        pointer = head
        
        while(pointer is not None):
            nextNode = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = nextNode
            
        return prev
    
x = ListNode(1)
x.next = ListNode(7)
x.next.next = ListNode(3)
x.next.next.next = ListNode(1)

y = ListNode(4)
y.next = ListNode(9)
y.next.next = ListNode(3)
y.next.next.next = ListNode(2)

x.next.next.next.next = y


print(Solution().pairSum(x))