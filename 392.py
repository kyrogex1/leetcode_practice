from typing import *

# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def __init__(self):
        self.lastSearchedIndex = 0
        
    def isSubsequence(self, s: str, t: str) -> bool:
        if (s == ""):
            return True
        
        # If substring of s is not a subsequence of t, then obviously s is not subsequence of t
        prevResults = self.isSubsequence(s[:-1], t)
        if (not prevResults):
            return False
        
        for i in range(self.lastSearchedIndex, len(t)):
            if (s[-1] == t[i]):
                self.lastSearchedIndex = i+1
                return True
            
        return False

# Solution that uses just one pass to solve. No DP required.
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if (s == ""):
#             return True
        
#         # Simple solution, for each char in s, we try to find char in t.
#         startingIndex = 0
#         for j, char1 in enumerate(s):
#             for i in range(startingIndex, len(t)):
#                 startingIndex += 1
#                 if (t[i] == char1):
#                     # If all chars in j has been found, return True
#                     if (j == len(s)-1):
#                         return True
#                     break
        
#         return False

        