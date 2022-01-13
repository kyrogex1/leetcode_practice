from typing import *

# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    # Solution is to traverse the whole array, and only update newIndex when a unique number is encountered.
    # When a new unique number is encountered, write it to newIndex.
    # Its easier to solve this problem by returning first k items, instead of trying to modify the array using pop()
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        newIndex = 0
        
        for num in nums:
            if (num != prev):
                prev = num
                nums[newIndex] = num
                newIndex += 1
                
        return newIndex
            
array = [1,1,1,2,3,3,3,4]
solution = Solution()
solution.removeDuplicates(array)
print(array)
