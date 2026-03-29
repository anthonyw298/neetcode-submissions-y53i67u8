# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Attempt 3
        if not list1:
            return list2
        elif not list2:
            return list1
        dummy=ListNode(0)
        curr=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                curr=curr.next
                list1=list1.next
            else:
                curr.next=list2
                curr=curr.next
                list2=list2.next
        if list1:
            curr.next=list1
        elif list2:
            curr.next=list2
        return dummy.next

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''dummy=ListNode(0)
        tail=dummy
        if not list1:
            return list2
        elif not list2:
            return list1
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1==None:
            while list2:
                tail.next=list2
                list2=list2.next
                tail=tail.next
        elif list2==None:
            while list1:
                tail.next=list1
                list1=list1.next
                tail=tail.next
        return dummy.next'''
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''if not list1:
            return list2
        elif not list2:
            return list1
        if head1.val>head2.val:
            currA=head2
            currB=head1
        else:
            currA=head1
            currB=head2
        #continue on same linked if its less then next 
        while currA or currB:
            if currA==None:
                while currB!=None:
                    currB=currB.next
            elif currB==None:
                while currA!=None:
                    currA=currA.next
            while currA.next.val<currB.val:
                currA=currA.next
            nxt=currA.next
            currA.next=currB
            currA=currA.next
            currB=nxt
        #do a redirect if its bigger'''
        