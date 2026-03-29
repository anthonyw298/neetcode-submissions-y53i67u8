# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        import heapq
        if not root:
            return
        heap=[]
        self.append(root,heap)
        print(heap,'heap')
        heapq.heapify(heap)
        for _ in range(k-1):
            x=heapq.heappop(heap)
            print(x)
        return heapq.heappop(heap)

    def append(self,root,heap):
        if not root:
            return
        heapq.heappush(heap,root.val)
        return self.append(root.left,heap) or self.append(root.right,heap)
        