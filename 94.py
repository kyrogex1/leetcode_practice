from typing import *

# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
      self.traversal = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if (root is None):
        return self.traversal
        
      self.inorderTraversal(root.left)   
      self.traversal.append(root.val)
      self.inorderTraversal(root.right)
      
      return self.traversal


solution = Solution()
answer = solution.isValidBST()
print(answer)