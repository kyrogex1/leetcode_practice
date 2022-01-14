from typing import *

# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.missing = []
        self.lca = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.missing.append(p)
        self.missing.append(q)
        self.traverse(root)

        return self.lca

    def traverse(self, root: 'TreeNode') -> bool:
        setLCA = False
        if (root is None):
            return setLCA

        # If either p or q is found, we remove it from self.missing
        # We also setLCA to true, because this node is now a possible LCA
        # All other possible LCAs only exist up the tree / greater ancestors
        if (root in self.missing):
            self.missing.remove(root)
            if (len(self.missing) == 1):
                setLCA = True

        # If either p or q is not yet found, search left subtree
        if (len(self.missing) > 0):
            setLCA = self.traverse(root.left) or setLCA #If setLCA was set True before (eg if root in self.missing == true), let it continue to be True

        # If either p or q is not yet found, search right subtree
        if (len(self.missing) > 0):
            setLCA = self.traverse(root.right) or setLCA #If setLCA was set True before (eg if traversing left subtree found a value), let it continue to be True

        # If both p and q are found, we set LCA if (setLCA true) and (self.lca has not been set before)
        if (len(self.missing) == 0):
            if (setLCA and self.lca is None):
                self.lca = root

        return setLCA
                 
solution = Solution()

## Binary Tree Setup
root = TreeNode(2)
root.left = TreeNode(1)

root.right = TreeNode(4)

# Try solution
answer = solution.lowestCommonAncestor(root, root.left, root)
print(answer) 