# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.most = float('-inf')
        self.dfs(root)
        return self.most
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.most = max(self.most, left + right + node.val)
        up = max(left, right) + node.val
        return up if up > 0 else 0









































        '''#Attempt 2
        if not root:
            return
        res=[root.val]
        def dfs(root):
            if not root:
                return 0
            leftMax=dfs(root.left)
            rightMax=dfs(root.right)
            leftMax=max(leftMax,0)
            rightMax=max(rightMax,0)
            res[0]=max(res[0],leftMax+rightMax+root.val)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''res=None
        if not res:
            print('hi')
        return res
        self.best = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.best = max(self.best, left + right + node.val)

            return node.val + max(left, right)

        dfs(root)
        return self.best'''


