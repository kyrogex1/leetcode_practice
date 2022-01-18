from typing import *

# 66. Plus One
# https://leetcode.com/problems/plus-one/

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        self.digits = digits
        shouldAddOneMoreDigit = self.traverse(0)
        if (shouldAddOneMoreDigit):
            digits.insert(0, 1)
        return digits
        
    def traverse(self, currentIdx: int) -> List[int]:
        ## Last digit has not been reached, increment by 1 if next digit adds up to 10
        if (currentIdx + 1 != len(self.digits)):
            increment = 1 if self.traverse(currentIdx + 1) else 0
        ## Last digit has been reached, always increment by 1
        else:
            increment = 1
        
        updatedDigit = self.digits[currentIdx] + increment
        if (updatedDigit == 10):
            self.digits[currentIdx] = 0
            return True
        else:
            self.digits[currentIdx] = updatedDigit

            
array = [1,3]
solution = Solution()
print(solution.searchInsert(array, -1))
print(array)
