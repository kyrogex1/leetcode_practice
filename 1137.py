from typing import *

# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class Solution:
    def __init__(self):
        self.cache = {0: 0, 1:1, 2: 1}
        
    def tribonacci(self, n: int) -> int:
        if (n in self.cache):
            return self.cache[n]
        result = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)        
        self.cache[n] = result
        return result