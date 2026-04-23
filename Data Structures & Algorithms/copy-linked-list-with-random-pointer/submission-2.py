"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy[curr].next = copy[curr.next] if curr.next else None
            copy[curr].random = copy[curr.random] if curr.random else None
            curr = curr.next
        return copy[head] if head else None
        
        
        
        









































        '''if not head:
            return None
        dic = {}
        dic[None] = None
        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            dic[curr].next = dic[curr.next]
            dic[curr].random = dic[curr.random]
            curr = curr.next
        return dic[head]'''

        