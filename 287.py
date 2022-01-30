from typing import *

# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = 0
        
        while(True):
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if (hare == tortoise):
                break
                
        entry = 0
        while(entry != tortoise):
            entry = nums[entry]
            tortoise = nums[tortoise]
            
        return tortoise

import random
number = 231
data = [x+1 for x in range(number)]
data.append(33)
random.shuffle(data)
print(Solution().findDuplicate(data))