# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque 
        if not root:
            return []
        lst=[]
        idx=0
        queue=deque([(root,root.val,idx)])
        while queue:
            root,valR,idx = queue.popleft()
            print(valR,idx)
            if len(lst)==idx:
                lst+=[[]]
            lst[idx]+=[valR]
            if root.left:
                queue.append((root.left,root.left.val,idx+1))
            if root.right:
                queue.append((root.right,root.right.val,idx+1))

        return lst
            