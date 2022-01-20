from typing import *

# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if (n in self.cache):
            return self.cache[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = result
        return result