from typing import *

# 1019. Next Greater Node In Linked List
# https://leetcode.com/problems/next-greater-node-in-linked-list/submissions/

# You are given the head of a linked list with n nodes.

# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)
        
class Solution:
    # Common misconception that looking at the stack on every node access
    # leads to O(n2) time complexity. But since each node is only
    # added / popped at most once, this means that its actually O(n) time complexity
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result, stack = [], []
        index = 0
        while(head):
            # Check which of the previous nodes are smaller than current pointer value
            # And update result array
            while(len(stack) > 0 and head.val > stack[-1]['val']):
                popped = stack.pop()
                result[popped['index']] = head.val
                
            result.append(0)
            stack.append({
                'index': index,
                'val': head.val,
            })      
            index += 1
            head = head.next
            
        return result

# x = ListNode(2)
# x.next = ListNode(7)
# x.next.next = ListNode(4)
# x.next.next.next = ListNode(3)
# x.next.next.next.next = ListNode(5)
# print(Solution().nextLargerNodes(x))