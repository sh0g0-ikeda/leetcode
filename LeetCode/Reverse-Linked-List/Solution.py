1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        current=head
9        prev=None
10        while current:
11            nex=current.next
12            current.next=prev
13            prev=current
14            current=nex
15
16        return prev