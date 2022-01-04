from typing import *

# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      return self.isValidBSTWrapper(root)[0]

    def isValidBSTWrapper(self, root: Optional[TreeNode]) -> Tuple[bool, int, int]:
      ## Terminating case for child of leave nodes
      if (root is None):
        return True, (2**31), -(2**31)

      isLeftSubtreeValid, leftSmallest, leftGreatest = self.isValidBSTWrapper(root.left)
      isLeftValid = isLeftSubtreeValid and (leftGreatest < root.val)
      leftSmallest = root.val if (leftSmallest == 2**31) else leftSmallest

      isRightSubtreeValid, rightSmallest, rightGreatest = self.isValidBSTWrapper(root.right)
      isRightValid = isRightSubtreeValid and (rightSmallest > root.val)
      rightGreatest = root.val if (rightGreatest == -(2**31)) else rightGreatest

      return (isLeftValid and isRightValid), leftSmallest, rightGreatest

solution = Solution()
answer = solution.isValidBST(TreeNode(-2147483648))
print(answer)