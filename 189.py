from typing import *

# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Avoid extra rotations since rotating more times than the length of the array just cycles through
        k = k % len(nums)

        # Reverse
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    # Helper method to reverse an array between a start and end index
    def reverse(self, nums: List[int], start: int, end: int):
        for i in range((end-start+1) // 2):
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]
        return
            
array = [1,2,3,4,5,6,7,8]
solution = Solution()
print(solution.rotate(array, 5))
print(array)

# Solution that uses O(n) space by duplicating the array
    # def rotate(self, nums: List[int], k: int) -> None:
#         copy = []
#         for x in nums:
#             copy.append(x)
            
#         k = k % len(nums)
#         for y in range(k):
#             nums[y] = copy[-k+y]
            
#         for y in range(len(nums) - k):
#             nums[k+y] = copy[y]