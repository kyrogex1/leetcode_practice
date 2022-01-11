from typing import *

# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedUnwrapped(root)[0]

    # Returns Tuple[isBalanced: bool, heightOfTree: int]
    def isBalancedUnwrapped(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        if (root is None):
            return True, 0

        leftIsBalanced, leftHeight = self.isBalancedUnwrapped(root.left)
        rightIsBalanced, rightHeight = self.isBalancedUnwrapped(root.right)
        
        heightDifference = leftHeight - rightHeight
        isBalanced = leftIsBalanced and rightIsBalanced and (-1 <= heightDifference) and (heightDifference <= 1)

        return isBalanced, max(leftHeight, rightHeight) + 1

solution = Solution()

## Binary Tree Setup
root = TreeNode(1)
root.left = TreeNode(2)
root.right = None

# Try solution
answer = solution.isBalanced(root)
print(answer)








# Misunderstood question
# This solution checks if the depth of ALL leafs nodes in a tree differ by at most 1.
# class Solution:
#     def __init__(self):
#         self.permissableHeights = []

#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         self.traverse(root, 0)

#     def traverse(self, root: Optional[TreeNode], prevHeight) -> bool:
#         currentHeight = prevHeight + 1

#         if (root is None):
#             # 0 Numbers in permissableNumbers
#             if (len(self.permissableHeights) == 0):
#                 self.permissableHeights.append(currentHeight)
#                 return True

#             ## 1 Number in permissableNumbers
#             elif (len(self.permissableHeights) == 1):
#                 firstPermissableHeight = self.permissableHeights[0]
#                 heightDifference = currentHeight - firstPermissableHeight
#                 if (-1 <= heightDifference and heightDifference <= 1 ):
#                     if (currentHeight not in self.permissableHeights):
#                         self.permissableHeights.append(currentHeight)
#                     return True
#                 else:
#                     return False

#             ## 2 Numbers are in permissableNumbers
#             else:
#                 return currentHeight in self.permissableHeights

#         checkLeftSubtree = self.traverse(root.left, currentHeight)
#         checkRightSubtree = self.traverse(root.right, currentHeight)

#         return checkLeftSubtree and checkRightSubtree