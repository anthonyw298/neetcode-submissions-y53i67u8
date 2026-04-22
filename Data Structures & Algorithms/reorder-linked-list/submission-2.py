# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        curr = head
        while curr and prev:
            tmpC = curr.next
            tmpP = prev.next
            curr.next = prev
            prev.next = tmpC
            curr, prev = tmpC, tmpP





































        '''#Attempt 3
        if not head:
            return
        mid,fast=head,head.next
        while fast and fast.next:
            mid=mid.next
            fast=fast.next.next
        prev=None
        second = mid.next
        mid.next = None
        mid = second
        while mid:
            tmp=mid.next
            mid.next=prev
            prev,mid=mid,tmp
        mid=prev
        while head and mid:
            tmp=mid.next
            temp=head.next
            head.next=mid
            head.next.next=temp
            mid=tmp
            head=temp

        if mid:
            head.next=mid

        return'''

        

        

















        
        
        #Attempt 2

        #Find Middle
        '''slow,fast= head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #Cut Link Off
        second=slow.next
        prev=slow.next=None

        #Reverse Second Half Link
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp

        #Merge List
        first,second = head , prev
        while second:
            temp1,temp2 = first.next, second.next
            first.next=second 
            second.next=temp1
            first, second = temp1, temp2 '''

        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''#dummary
        count,cnt=0,0
        back,headd=head,head
        #traverse and get a count
        while back:
            count+=1
            back=back.next
        while cnt<=(count-1)//2:
            if cnt==0:
                dummy=ListNode(headd.val)
                tail=dummy
            headd=headd.next
            cnt+=1
        tail.next=headd#maybe while it

        dummyr=ListNode(0)
        tailr=dummyr
        while tail:
            if count%2==0:
                tailr.next=head
                tailr=tailr.next
                head=head.next
            else:
                tailr.next=tail
                tailr=tailr.next
                tail=tail.next
            count-=1

        #then traverse again to middle
        #after middle reverse all nodes then dummy store connect 
        #traverse one more merging two lists'''
