from typing import *

# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0

        leftMaxDepth = self.maxDepth(root.left) + 1
        rightMaxDepth = self.maxDepth(root.right) + 1

        return max(leftMaxDepth, rightMaxDepth)

solution = Solution()
answer = solution.isValidBST()
print(answer)