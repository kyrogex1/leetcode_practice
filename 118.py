from typing import *

# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if (j == 0):
                    row.append(1)
                elif (j == i):
                    row.append(1)
                else:
                    row.append(prev[j-1] + prev[j])
            answer.append(row)
            prev = row
        
        return answer
  
array = [1,3]
solution = Solution()
print(solution.generate(6))
print(array)
