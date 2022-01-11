from typing import *

# 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Given a binary tree, find its minimum depth.

# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return self.isCompleteTreeUnwrapped(root, 0, [])[0] 


    # This problem can be solved as such
    # 1. Use DFS, Find the height of the left mode leaf node. This gives the deepest permissableHeight, X, and the height of all subsequent leaf nodes traversed must be X or one less than X ie. [X, X-1]
    # 2. Access the next leaf node, if the depth is equal X, return True and permissableHeights is still [X, X-1]
    # 3. If the depth is equal X-1, return True. This means that the height of all subsequent leaf nodes must be = X-1
    # 4 If the depth is not in permissableHeights, return False
    def isCompleteTreeUnwrapped(self, root: Optional[TreeNode], currentHeight, permissableHeights) -> Tuple[bool, List[int]]:
        if (root is None):

            # Case when accessing the left most leaf node, append X-1 and X
            if (len(permissableHeights) == 0):
                permissableHeights.append(currentHeight - 2) # Must minus 1 or 2 here, since technically root is None, and should not contribute to height
                permissableHeights.append(currentHeight - 1)
                return True, permissableHeights

            # Case when accessing any node other than left most leaf node
            elif (currentHeight - 1 in permissableHeights):

                # Case when height = X-1
                if (currentHeight - 1 == permissableHeights[0]):
                    permissableHeights = []
                    permissableHeights.append(currentHeight - 1)
                    return True, permissableHeights

                # Case when permissableHeights has only 1 value ie X-1
                else:
                    return True, permissableHeights
            else:
                return False, []
                
        isLeftSideValid, nextLeafValidHeights = self.isCompleteTreeUnwrapped(root.left, currentHeight + 1, permissableHeights)
        if (not isLeftSideValid):
            return False, []
        
        isRightSideValid, nextLeafValidHeights = self.isCompleteTreeUnwrapped(root.right, currentHeight + 1, nextLeafValidHeights)
        if (not isRightSideValid):
            return False, []

        return True, nextLeafValidHeights


solution = Solution()

## Binary Tree Setup
root = TreeNode(1)
root.left = TreeNode(2)
root.right = None

# Try solution
answer = solution.isBalanced(root)
print(answer)