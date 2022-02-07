from typing import *

# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Definition for singly-linked list.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        generated = self.generateNextGreaterHashmap(nums2)
        return [generated[num] for num in nums1]
    
    # Generates a hashMap of nums2. Each key corresponds to a unique
    # element in nums2. The value stored in the hashmap represents
    # the next greater element for the given key.
    # See 1019. Next Greater Node In Linked List for reference
    def generateNextGreaterHashmap(self, nums: List[int]) -> List[int]:
        result, stack = {}, []
        
        for num in nums:
            while(len(stack) > 0 and num > stack[-1]):
                result[stack.pop()] = num
            result[num] = -1
            stack.append(num)
            
        return result