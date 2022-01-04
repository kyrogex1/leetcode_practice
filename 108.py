from typing import *

# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
      print(nums)
      if (len(nums) == 0):
        return TreeNode(None)
      
      if (len(nums) == 1):
        return TreeNode(nums[0])

      if (len(nums) == 2):
        left = TreeNode(nums[0])
        return TreeNode(nums[1], left)

      midIdx = len(nums) // 2
      mid = nums[midIdx]

      left = self.sortedArrayToBST(nums[: midIdx])
      right = self.sortedArrayToBST(nums[midIdx + 1:])
      node = TreeNode(mid, left, right)

      return node




solution = Solution()
answer = solution.sortedArrayToBST([-10,-3,0,5,9])
print(answer)