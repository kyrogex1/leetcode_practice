from typing import *

# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if (j == 0):
                    row.append(1)
                elif (j == i):
                    row.append(1)
                else:
                    row.append(prev[j-1] + prev[j])
            prev = row
        
        return row
  
array = [1,3]
solution = Solution()
print(solution.getRow(0))
print(array)
