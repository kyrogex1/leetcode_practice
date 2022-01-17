from typing import *

# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

class Solution:
    def __init__(self):
        self.cache = {0:1}
        self.numOfSubarraysThatSumK = 0

    def subarraySum(self, nums: List[int], k: int) -> int:
        totalSum = 0

        for num in nums:
            totalSum += num
            difference = totalSum - k
            
            if (difference in self.cache):
                numSubarraysThatSumDifference = self.cache[difference]
                self.numOfSubarraysThatSumK += numSubarraysThatSumDifference

            frequency_of_sum = self.cache.get(totalSum, 0)
            self.cache[totalSum] = frequency_of_sum + 1

        return self.numOfSubarraysThatSumK

                

solution = Solution()

# Try solution
answer = solution.subarraySum([1,2,1,2,1], 3)
print(answer)