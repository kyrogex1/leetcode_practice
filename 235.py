from typing import *

# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

#     1. Search for a node to remove.
#     2. If the node is found, delete the node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pointer = root
        smaller = p if (q.val > p.val) else q
        larger = p if (q.val < p.val) else q
        nodeStack = []
        upperLimit = 10**10
        lowerLimit = upperLimit * -1

        while(pointer != smaller):
            nodeStack.append((pointer, lowerLimit, upperLimit))
            if (pointer.val > smaller.val):
                upperLimit = pointer.val - 1
                pointer = pointer.left
            else:
                lowerLimit = pointer.val + 1
                pointer = pointer.right

        nodeStack.append((pointer, lowerLimit, upperLimit))

        while(len(nodeStack) != 0):
            pointer, lowerLimit, upperLimit = nodeStack[-1]
            if (larger.val > upperLimit):
                nodeStack.pop()
            else:
                return pointer

        return root
        
solution = Solution()

## Binary Tree Setup
root = TreeNode(2)
root.left = TreeNode(1)

root.right = TreeNode(4)

# Try solution
answer = solution.lowestCommonAncestor(root, root.left, root)
print(answer)





# Wrong solution that i came up with
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         smaller = q if (p.val > q.val) else p
#         larger = q if (p.val < q.val) else p
#         pointer = root
#         nodeStack = []

#         while(pointer != smaller):
#             nodeStack.append(pointer)
#             if (smaller.val < pointer.right.val):
#                 pointer = pointer.left
#             else:
#                 pointer = pointer.right
        
#         nodeStack.append(pointer)

#         while(nodeStack[-1] != root):
#             pointer = nodeStack[-1]
#             nodeStack.pop()
#             if (larger.val >= nodeStack[-1].val):
#                 continue
#             else:
#                 return pointer    