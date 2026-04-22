# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        return prev
            








































        '''#Attempt 2
        if not head:
            return
        prev=None
        while head:
            temp=head.next
            head.next=prev
            prev,head=head,temp
        head=prev
        return head'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''if not head:
            return
        if not head.next:
            return head
        current=head
        second=current.next
        while current.next:
            if current==head:
                first=current
                current=current.next.next
                second.next=first
            else:
                after=current.next
                current.next=second
                second=current
                current=after
        current=head
        current.next=second
        return head'''
            
        