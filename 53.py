from typing import *

# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -1 * 10**5
        currentSum = 0
        
        for num in nums:
            currentSum += num
            maximum = max(maximum, currentSum)

            # If current sum is negative, dispose of all previously accumulated numbers and set currentSum to 0
            if (currentSum < 0):
                currentSum = 0
            
        return maximum