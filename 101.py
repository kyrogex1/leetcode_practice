from typing import *

# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftSubtree = root.left
        rightSubtree = root.right
        return self.areBothTreesSymmetric(leftSubtree, rightSubtree)

    def areBothTreesSymmetric(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # If both p and q are leaves, return True
        if (p is None and q is None):
            return True
        
        # If one of them is None, and the other is not, return False
        if (p is None or q is None):
            return False

        # If their values are not equal, return False
        if (p.val != q.val):
            return False


        ## 2 Trees, p and q, are considered symmetric if (left of p) equivalent to (right of p) AND (right of p) equivalent to (left of q)
        ## Is left of p equivalent to right of q
        areTreesSymmetric1 = self.areBothTreesSymmetric(p.left, q.right)

        ## Is right of p equivalent to left of q
        areTreesSymmetric2 = self.areBothTreesSymmetric(p.right, q.left)

        return areTreesSymmetric1 and areTreesSymmetric2

solution = Solution()
answer = solution.isValidBST()
print(answer)