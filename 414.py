from typing import *

# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximums = self.findKMaximumNumber(nums, 3)
        return maximums[-1] if (maximums[-1] is not None) else maximums[0]

    def findKMaximumNumber(self, nums: List[int], k: int) -> List[int]:
        maximums = [None for i in range(k)]
        for num in nums:
            for i in range(len(maximums)):
                # If number is already in maximums, terminate
                if (maximums[i] == num):
                    break
                if (maximums[i] is None or num > maximums[i]):
                    for j in range(len(maximums)-1, i, -1):
                        maximums[j] = maximums[j-1]
                    maximums[i] = num
                    break
        
        return maximums


        
  
array = [1,3]
solution = Solution()
print(solution.thirdMax([2,2,3,1]))
print(array)
