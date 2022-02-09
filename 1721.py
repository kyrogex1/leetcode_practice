from typing import *

# 1721. Swapping Nodes in a Linked List
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tortoise = hare = head
        for _ in range(k):
            hare = hare.next
           
        lhs = None
        while(hare):
            if (k == 1):
                lhs = tortoise
            k -= 1
            tortoise = tortoise.next
            hare = hare.next
        rhs = tortoise
        
        while(k > 1):
            tortoise = tortoise.next
            k-= 1
        lhs = lhs if lhs else tortoise
        
        lhs.val, rhs.val = rhs.val, lhs.val
        
        return head
        
# x = ListNode(1)
# x.next = ListNode(2)
# x.next.next = ListNode(3)
# x.next.next.next = ListNode(4)
# x.next.next.next.next = ListNode(5)

# print(Solution().swapNodes(x, 5))