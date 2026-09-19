# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        a = head
        b = dummy
        while n > 0:
            a = a.next
            n -= 1
        while a:
            a = a.next
            b = b.next
        b.next = b.next.next
        return dummy.next
