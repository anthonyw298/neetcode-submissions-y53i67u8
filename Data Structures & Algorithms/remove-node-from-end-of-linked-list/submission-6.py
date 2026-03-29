# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Attempt 3
        if not head:
            return
        fast=head
        while n!=1:
            fast=fast.next
            n-=1
        prev=None
        slow=head
        while fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next
        if slow==head:
            return head.next
        prev.next=slow.next
        slow.next=None
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''dummy=ListNode(0,head)
        left=dummy
        right=head
        while n>0:
            right=right.next
            n-=1
        while right:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next'''

















        

        #Attempt 1
        '''curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        count=1
        curr,prev=prev,None
        while curr:
            if count==n:
                print('bruh')
                if curr==head and prev== None:
                    return
                elif curr==head:
                    prev=head
                    prev.next=None
                else:
                    print('hit')
                    tmp=curr.next
                    tmp.next=prev
                    curr=tmp
            else:
                prev=curr
                temp=curr.next
                print(temp.val)
                curr.next=prev
                curr=temp.next

            count+=1
        
        return head'''