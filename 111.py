from typing import *

# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.minimumDepth = 10**6

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0

        self.traverse(root, 0)
        return self.minimumDepth

    def traverse(self, root: Optional[TreeNode], prevDepth):
        if (root is None):
            return
        
        currentDepth = prevDepth + 1

        if (currentDepth > self.minimumDepth):
            return

        if (root.left is None and root.right is None):
            self.minimumDepth = currentDepth
            return

        self.traverse(root.left, currentDepth)
        self.traverse(root.right, currentDepth)

        return

solution = Solution()

## Binary Tree Setup
root = TreeNode(1)
root.left = TreeNode(2)
root.right = None

# Try solution
answer = solution.isBalanced(root)
print(answer)