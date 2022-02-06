from typing import *

# 817. Linked List Components [Re-Do]
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

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
class Solution:
    # True O(1) Space solution. We dont need stack / queue here to traverse
    # the tree because we make of the .next pointers to locate the next
    # node to traverse to
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (root is None):
            return None
        
        nextNode = root
        mostLeftChildInNextLevel = None
        while(nextNode.left):
            nextNode.left.next = nextNode.right
            if (nextNode.next):
                nextNode.right.next = nextNode.next.left
            
            if (mostLeftChildInNextLevel is None):
                mostLeftChildInNextLevel = nextNode.left
                
            if (nextNode.next):
                nextNode = nextNode.next
            else:
                nextNode = mostLeftChildInNextLevel
                mostLeftChildInNextLevel = None
                
        return root
        
    # DFS Solution that uses O(1) Space, but o(lgN) stack space
    # Basically, parent node sets the next of its children
    # - root.left.next = root.right
    # - root.right.next = root.next.left
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if (root is None):
#             return root
#         left, right, neighbour = root.left, root.right, root.next
        
#         if left:
#             left.next = right
#             if (neighbour):
#                 right.next = neighbour.left
#             self.connect(left)
#             self.connect(right)
            
#         return root
            
        