from typing import *

# 117. Populating Next Right Pointers in Each Node II [Re-Do]
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Given a binary tree

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

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

    def __repr__(self):
        return str(self.val)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if (root is None):
            return root
        
        # Leaf node, dont do anything
        if (root.left is None and root.right is None):
            return root
        
        if (root.left):
            if (root.right):
                root.left.next = root.right
                pointToNextNodesChild = root.right
            else:
                pointToNextNodesChild = root.left
        # Set to next's first child
        else:
            pointToNextNodesChild = root.right
        
        nextNode = root.next
        nextSet = False
        while (nextNode and not nextSet):
            if (nextNode.left):
                pointToNextNodesChild.next = nextNode.left
                nextSet = True
            elif (nextNode.right):
                pointToNextNodesChild.next = nextNode.right
                nextSet = True
            else:
                nextNode = nextNode.next
        
        self.connect(root.right)
        self.connect(root.left)
        
        return root
            
# x = Node(1)
# x.left = Node(2)
# x.right = Node(3)
# x.left.left = Node(4)
# # x.right.right = Node(5)
# x.left.left.left = Node(6)
# # x.right.right.right = Node(7)

# x = Node(2)
# x.left = Node(1)
# x.right = Node(3)
# x.left.left = Node(0)
# x.left.right = Node(7)
# x.right.left = Node(9)
# x.right.right = Node(1)
# x.left.left.left = Node(2)
# x.left.right.left = Node(1)
# x.left.right.right = Node(0)
# x.right.right.left = Node(8)
# x.right.right.right = Node(8)

# solution = Solution().connect(x)
# print(solution.left.right.right.next)