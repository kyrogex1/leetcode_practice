from typing import *

# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 0):
            return 1
        
        if (n == 1):
            return x
        
        if (n == -1):
            return 1/x
        
        resultOfHalf = self.myPow(x, n // 2)
        fullResult = resultOfHalf * resultOfHalf
        if (n % 2 == 1):
            fullResult = fullResult * x
            
        return fullResult
        