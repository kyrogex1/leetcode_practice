from typing import *

# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
      self.traversal = []
      self.queue = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      self.queue.append(root)
      while (len(self.queue) > 0):
        currentLevelTraversal = self.traverseLevel()
        if (len(currentLevelTraversal) > 0):
          self.traversal.append(currentLevelTraversal)
      
      return self.traversal

    def traverseLevel(self):
      nextLevelQueue = []
      currentLevelTraversal = []
      for node in self.queue:
        if (node is None):
          continue

        nextLevelQueue.append(node.left)
        nextLevelQueue.append(node.right)
        currentLevelTraversal.append(node.val)

      self.queue = nextLevelQueue
      return currentLevelTraversal


# BFS Traversal if the expected result is just order of traversal, ie return type of levelOrder is List[int] instead of List[List[int]]
# class Solution:

#     def __init__(self):
#       self.traversal = []
#       self.queue = []

#     def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
#       self.queue.append(root)
#       while(len(self.queue) > 0):
#         node = self.queue[0]
#         self.queue.pop(0)
#         if (node is None):
#           continue

#         self.queue.append(node.left)
#         self.queue.append(node.right)
#         self.traversal.append(node.val)

#       return self.traversal

solution = Solution()
answer = solution.isValidBST()
print(answer)