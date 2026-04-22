# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while fast and slow != fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        if not fast:
            return False
        return True

        



































        '''#Attempt 2
        if not head:
            return False
        slow=head
        fast=head.next
        while fast and fast.next:
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False'''













        
        
        
        
        
        #Attempt 1
        #reverse a linked list adn if one already connected at the end the return true
        '''prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            if curr==head:
                return True

        return False'''