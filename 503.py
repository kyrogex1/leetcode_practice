from typing import *

# 503. Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result, stack = [], []
        
        for i in range(len(nums) * 2):
            currentIdx = i % len(nums)

            while (len(stack) > 0 and nums[currentIdx] > stack[-1]['val']):
                popped = stack.pop()
                result[popped['idx']] = nums[currentIdx]
            
            if (i < len(nums)):
                result.append(-1)
                stack.append({
                    'idx': currentIdx,
                    'val': nums[currentIdx]
                })
            
        return result
            

# [1, 2, 3, 4, 3]