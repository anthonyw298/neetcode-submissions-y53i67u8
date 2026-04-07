import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Attempt 3
        heap=[]
        for LL in lists:
            curr=LL
            while curr:
                heapq.heappush(heap,curr.val)
                curr=curr.next
        dummy=ListNode(0)
        curr=dummy
        while heap:
            val = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr=curr.next
        return dummy.next

































        
        
        
        '''#Attempt 2
        import heapq
        heap=[]
        for LL in lists:
            while LL:
                heapq.heappush(heap,LL.val)
                LL=LL.next
        dummy=ListNode(0)
        curr=dummy
        while heap:
            curr.next=ListNode(heapq.heappop(heap))
            curr=curr.next
        return dummy.next'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''dummy=ListNode(0)
        l=dummy
        #have,need=0,len(lists)
        for idx,LL in enumerate(lists):
            head=LL
            if idx==0:
                while head:
                    l.next=head
                    l=l.next
                    head=head.next
            else:
                r=dummy.next
                l=dummy
                while r and head:
                    if head.val<=r.val:
                        temp=head.next
                        l.next=head
                        l=l.next
                        l.next=r
                        head=temp
                        print('less')
                    else:
                        while head.val>r.val:
                            print('greater')
                            l=l.next
                            r=r.next
                            if not r:
                                break
                if head:
                    l.next=head
        return dummy.next'''