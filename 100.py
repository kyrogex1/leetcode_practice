from typing import *

# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if (p is None and q is None):
        return True

      if (p is None or q is None):
        return False
      
      if (p.val != q.val):
        return False
        
      isLeftSameTree = self.isSameTree(p.left, q.left)   
      isRightSameTree = self.isSameTree(p.right, q.right)
      
      return isLeftSameTree and isRightSameTree


solution = Solution()
answer = solution.isValidBST()
print(answer)