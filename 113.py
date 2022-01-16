from typing import *

# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.paths = []
        self.currentPath = []
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.traverse(root, targetSum)
        return self.paths
        
    def traverse(self, root: Optional[TreeNode], targetSum: int):
        if (root is None):
            return
        
        # If child node, check if targetSum is achieved
        if (root.left is None and root.right is None):
            if (targetSum == root.val):
                self.paths.append(self.currentPath + [root.val])
            return
        
        self.currentPath.append(root.val)
        childTargetSum = targetSum - root.val
        self.traverse(root.left, childTargetSum)
        self.traverse(root.right, childTargetSum)
        
        # Pop current node value before passing back control to parent
        self.currentPath.pop()
        
        return