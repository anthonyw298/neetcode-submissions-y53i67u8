# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next   # save next
            current.next = prev        # reverse pointer
            prev = current             # move prev forward
            current = next_node        # move current forward

        return prev  # prev is new head
            
        