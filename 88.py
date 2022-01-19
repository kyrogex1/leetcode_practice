from typing import *

# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:

    ## To solve this problem, fill the array from the back. This is so we can avoid swapping around which occurs when
    ## we try to fill in the from the front of the array
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while(m > 0 and n > 0):
            if (nums1[m-1] > nums2[n-1]):
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        # Exhaust nums2 if nums1 has been exhausted
        while(n > 0):
            nums1[m+n-1] = nums2[n-1]
            n -= 1

        # No need to exhaust nums1, since it is already sorted in nums1



        
solution = Solution()
print(solution.merge([1,2,5,6,9,10, 0, 0, 0, 0], 6, [3,4,7,8], 4))
