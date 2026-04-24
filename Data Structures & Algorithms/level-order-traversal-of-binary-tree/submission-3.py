# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, res = deque([]), []
        queue.append((root.val, 0, root))
        while queue:
            val, lvl, node = queue.popleft()
            if lvl >= len(res):
                res.append([])
            res[lvl].append(val)
            if node.left:
                queue.append((node.left.val, lvl + 1, node.left))

            if node.right:
                queue.append((node.right.val, lvl + 1, node.right))
        return res
        

        







































        '''from collections import deque
        queue = []
        res = []
        if not root:
            return queue
        queue = deque([])
        queue.append((root,0))
        while queue:
            node, lvl = queue.popleft()
            if lvl >= len(res):
                res.append([])
            res[lvl].append(node.val)
            if node.left:
                queue.append((node.left, lvl+1))
            if node.right:
                queue.append((node.right,lvl+1))
        return res'''




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''from collections import deque
        lst=[]
        if not root:
            return []
        queue=deque([(root,0)])
        while queue:
            node,idx=queue.popleft()
            print(node.val,idx)
            if idx>=len(lst):
                lst+=[[node.val]]
            else:
                lst[idx]+=[node.val]
            if node.left:
                queue.append((node.left,idx+1))
            if node.right:
                queue.append((node.right,idx+1))
        return lst'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''from collections import deque 
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

        return lst'''
            