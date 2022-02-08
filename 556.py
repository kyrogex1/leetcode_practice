from re import I
from typing import *

# 556. Next Greater Element III [Re-Do]
# https://leetcode.com/problems/next-greater-element-iii/

# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = self.intToArray(n)
        cache = {arr[len(arr) - 1]: len(arr) - 1}
    
        # Find the first digit that is smaller than RHS.
        # The only way to get a bigger digit is by swapping
        # with a bigger digit on RHS
        # Start from second last digit
        idx = len(arr) - 2
        while(idx >= 0 and arr[idx] >= arr[idx + 1]):
            if (arr[idx] not in cache):
                cache[arr[idx]] = idx
            idx -= 1
        
        # If no digit found, eg 751. Means n is already the largest number that can be formed from its digits
        if (idx < 0):
            return -1

        # Find the first digit, lookingVal (and its idx, idxToSwapWith) which is larger than arr[idx]
        lookingVal = arr[idx] + 1
        while (lookingVal < 10):
            if (lookingVal in cache):
                idxToSwapWith = cache[lookingVal]
                break
            lookingVal += 1

        # Swap idx and idxToSwapWith
        arr[idx], arr[idxToSwapWith] = arr[idxToSwapWith], arr[idx]

        # Perform reverse on arr[idx+1:]
        arr = arr[:idx+1] + arr[idx+1:][::-1]
        answer =  self.arrToInt(arr)
        if (answer > 2147483647):
            return -1
        else:
            return answer
        
    def intToArray(self, n: int) -> List[int]:
        result = []
        while (n > 0):
            remainder = n % 10
            result.insert(0, remainder)
            n = n // 10
            
        return result

    def arrToInt(self, arr: List[int]) -> int:
        result = 0
        exponent = 0
        while(arr):
            current = arr.pop()
            result += current * 10 ** exponent
            exponent += 1
        
        return result