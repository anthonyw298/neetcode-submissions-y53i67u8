# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
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
        return dummy.next