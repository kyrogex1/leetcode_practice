from typing import *

# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        int1 = self.linkedListToInt(l1)
        int2 = self.linkedListToInt(l2)
        resultSum = int1 + int2
        return self.intToLinkedList(resultSum)
        
    def intToLinkedList(self, integer):
        firstRun = True
        
        while (True):
            digit = integer % 10
            node = ListNode(digit)
            
            if (firstRun):
                head = node
                firstRun = False
            else:
                prev.next = node
            prev = node
            
            integer = integer // 10
            if (integer <= 0):
                break
                
        return head
            
    
    def linkedListToInt(self, head):
        power = 0
        result = 0
        while(head is not None):
            result += head.val * 10 ** power
            power += 1
            head = head.next
            
        return result
    
x = ListNode(9)
x.next = ListNode(9)
x.next.next = ListNode(9)
x.next.next.next = ListNode(9)
x.next.next.next.next = ListNode(9)

y = ListNode(9)
y.next = ListNode(9)

print(Solution().addTwoNumbers(x, y))