from typing import *

# 112. Path Sum
# https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If initial root is None, or traversed to a node that only has 1 child
        if (root is None):
            return False

        # Traverse until leaf Node
        if (root.left is None and root.right is None):
            if (targetSum - root.val == 0):
                return True
            else:
                return False

        leftHasPathSum = self.hasPathSum(root.left, targetSum - root.val)
        if (leftHasPathSum):
            return leftHasPathSum

        rightHasPathSum = self.hasPathSum(root.right, targetSum - root.val)
        if (rightHasPathSum):
            return rightHasPathSum

        return False
        

solution = Solution()

## Binary Tree Setup
root = TreeNode(1)
root.left = TreeNode(2)
root.right = None

# Try solution
answer = solution.isBalanced(root)
print(answer)
