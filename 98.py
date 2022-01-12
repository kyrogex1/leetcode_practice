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
            return self.isValidBSTUnwrapped(root)[0]

        def isValidBSTUnwrapped(self, root: Optional[TreeNode]) -> Tuple[bool, int, int]:
            # Set smallest and greatest to be None so that leaf node can set the actual value to itself.
            if (root is None):
                return True, None, None

            leftIsValidBST, leftSmallest, leftGreatest = self.isValidBSTUnwrapped(root.left)
            rightIsValidBST, rightSmallest, rightGreatest = self.isValidBSTUnwrapped(root.right)

            isTreeValid = (rightIsValidBST and leftIsValidBST) and (leftGreatest is None or leftGreatest < root.val) and (rightSmallest is None or rightSmallest > root.val)

            # If leaf node, set leftSmallest and rightGreatest to root.val
            if (rightGreatest is None):
                rightGreatest = root.val
            if (leftSmallest is None):
                leftSmallest = root.val

            return isTreeValid, leftSmallest, rightGreatest

solution = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

answer = solution.isValidBST(root)
print(answer)