from typing import *

# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
      self.traversal = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if (root is None):
        return self.traversal

      self.traversal.append(root.val) 
      self.preorderTraversal(root.left)
      self.preorderTraversal(root.right)
      
      return self.traversal


solution = Solution()
answer = solution.isValidBST()
print(answer)