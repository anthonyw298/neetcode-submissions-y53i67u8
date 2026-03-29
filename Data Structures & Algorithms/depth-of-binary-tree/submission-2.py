# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Attempt 3 - Stack
        if not root:
            return 0
        stack=[(root,1)]
        res=0
        while stack:
            node,val=stack.pop()
            res=max(res,val)
            if node.left:
                stack.append((node.left,val+1))
            if node.right:
                stack.append((node.right,val+1))
        return res
        #Attempt 2 - BFS
        '''from collections import deque
        if not root:
            return 0

        queue=deque([(root,1)])
        res=0
        while queue:
            node,val=queue.popleft()
            res=max(res,val)
            if node.left:
                queue.append((node.left,val+1))
            if node.right:
                queue.append((node.right,val+1))
        return res
            '''


        #Attempt 1-DFS
        '''if not root:
            return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)'''
        
        