# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.count += 1
            if self.count ==  k:
                self.res = node.val
                return
            dfs(node.right)
            return
        dfs(root)
        return self.res































        '''#Attempt 3
        stack=[]
        curr=root
        cnt=0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            cnt+=1
            if cnt==k:
                return curr.val
            curr=curr.right
'''
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''n=0
        stack=[]
        cur=root
        while cur and stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur=cur.right'''
        #Attempt 1
        '''import heapq
        if not root:
            return
        heap=[]
        self.append(root,heap)
        print(heap,'heap')
        for _ in range(k-1):
            x=heapq.heappop(heap)
            print(x)
        return heapq.heappop(heap)

    def append(self,root,heap):
        if not root:
            return
        heapq.heappush(heap,root.val)
        return self.append(root.left,heap) or self.append(root.right,heap)'''
        