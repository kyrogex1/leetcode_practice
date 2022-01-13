from typing import *

# 783. Minimum Distance Between BST Nodes
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.minDiff = 10**6
        self.prevNodeValue = None

    # Simple, just use inorder traversal to get retrieve nodes in ascending order
    # During the visit of each node
    #   1. We find the difference in value between the current visited node and the previous visited node. Then update self.minDiff
    #   2. we store its value in prevNodeValue
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return None
        
        self.minDiffInBST(root.left)
        if (self.prevNodeValue is not None):
            self.minDiff = min(self.minDiff, root.val - self.prevNodeValue)
        self.prevNodeValue = root.val
        self.minDiffInBST(root.right)

        return self.minDiff

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