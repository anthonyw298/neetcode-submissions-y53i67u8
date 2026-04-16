# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        curr = dummy
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            l1, l2, curr = l1.next, l2.next, curr.next
        while l1:
            total = l1.val + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            l1, curr = l1.next, curr.next
        while l2:
            total = l2.val + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            l2, curr = l2.next, curr.next
        if carry:
            curr.next  = ListNode(1)
        return dummy.next
