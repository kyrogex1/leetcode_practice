from typing import *

# 1646. Get Maximum in Generated Array
# https://leetcode.com/problems/get-maximum-in-generated-array/

# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

#     nums[0] = 0
#     nums[1] = 1
#     nums[2 * i] = nums[i] when 2 <= 2 * i <= n
#     nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

# Return the maximum integer in the array nums​​​.

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        current = 0
        nums = []
        while(current < n + 1):
            if (current == 0):
                nums.append(0)
            elif (current == 1):
                nums.append(1)
            else:
                quotient = current // 2
                remainder = current % 2
                isOdd = remainder == 1
                if (isOdd):
                    nums.append(nums[quotient] + nums[quotient + 1])
                else:
                    nums.append(nums[quotient])
            current += 1
                
        return max(nums)
            
            