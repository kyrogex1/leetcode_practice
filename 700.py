from typing import *

# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pointer = root
        while (pointer != None):
            if (pointer.val == val):
                return pointer
            else:
                if (val < pointer.val):
                    pointer = pointer.left
                else:
                    pointer = pointer.right
        
        return None


solution = Solution()

## Binary Tree Setup
root = TreeNode(3)

root.left = TreeNode(1)
root.left.left = None
root.left.right = TreeNode(2)

root.right = TreeNode(4)

# Try solution
answer = solution.lowestCommonAncestor(root, root.left.right, root)
print(answer)