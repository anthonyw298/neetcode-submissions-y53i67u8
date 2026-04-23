class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(curr):
            tail = curr
            group_head = curr
            count = 0
            while tail and count < k:
                count += 1
                tail = tail.next
            if count < k:
                return None
            prev = None
            while curr and count:
                count -= 1
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev, group_head, tail

        newHead = None
        prevTail = None
        curr = head
        while True:
            result = reverse(curr)
            if not result:
                if prevTail:
                    prevTail.next = curr
                break
            prev, group_head, curr = result
            if not newHead:
                newHead = prev
            else:
                prevTail.next = prev
            prevTail = group_head

        return newHead