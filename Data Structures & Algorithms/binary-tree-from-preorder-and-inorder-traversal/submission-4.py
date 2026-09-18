# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderMap = {}
        for idx, val in enumerate(inorder):
            self.inorderMap[val] = idx
        return self.dfs(0,0,len(inorder) - 1)
        
    def dfs(self, preStart, inStart, inEnd):
        if inStart > inEnd:
            return None
        val = preorder[preStart]
        root = TreeNode(val)
        mid = self.inorderMap[val]
        root.left = self.dfs(preStart + 1, inStart, mid - 1)
        root.right = self.dfs(preStart + (mid - inStart) + 1, mid + 1, inEnd)
        return root







































        '''if not inorder or not preorder:
            return None

        dic = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None

            # create root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = dic[root_val]

            # build subtrees
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)'''
        
        
        
        
        
        
        
        
        #Attempt 3
        '''indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)'''

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''if not preorder or not inorder:
            return None
        dic={}
        for i in range(len(inorder)):
            dic[inorder[i]]=i
        root=TreeNode(preorder[0])
        l,mid,r=0,dic[preorder[0]],len(inorder)-1
        dic[preorder[0]]==-1
        root.left=self.left(l,preorder)
        root.right=self.right(r,preorder)
        return root
    def left(l,preorder):
        if dic[preorder[l]]==-1:
            return None
        dic[preorder[l]]+=1
        root=TreeNode(preorder[l])
        root.left=self.left(l,preorder)
        root.right=self.right(r,preorder)

    def right(r,preorder):
        if dic[preorder[r]]==-1:
            return None
        dic[preorder[r]]+=1
        root=TreeNode(preorder[r])
        root.left=self.left(l,preorder)
        root.right=self.right(r,preorder)'''










        #Attempt 1
        '''if not preorder or not inorder:
            return None

        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        root = TreeNode(preorder[0])
        mid = dic[root.val]

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root'''


