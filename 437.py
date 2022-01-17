from typing import *

# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution algorithm from here. They both explain the same algorithm, albeit in a different way.
# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison
# https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
class Solution:
    def __init__(self):
        # Cache stores the frequency of the sum of all previous paths
        # Eg {5: 3} means there are 3 previous paths whose nodes sum up to 5
        self.cache = {0:1} 
        self.numberOfPaths = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.traverse(root, 0)

        return self.numberOfPaths

    def traverse(self, root: Optional[TreeNode], sum_so_far: int) -> int:
        if (root is None):
            return

        sum_of_current_path = sum_so_far + root.val
        sum_of_old_path = sum_of_current_path - self.targetSum
        if (sum_of_old_path in self.cache):
            num_paths = self.cache[sum_of_old_path]
            self.numberOfPaths += num_paths

        self.cache[sum_of_current_path] = self.cache.get(sum_of_current_path, 0) + 1
        self.traverse(root.left, sum_so_far + root.val)
        self.traverse(root.right, sum_so_far + root.val)
        self.cache[sum_of_current_path] = self.cache[sum_of_current_path] - 1

solution = Solution()

## Binary Tree Setup
root = TreeNode(5)
root.left = TreeNode(3)

# Try solution
answer = solution.pathSum(root, 8)
print(answer)