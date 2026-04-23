# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        if not root and subRoot:
            return False
        elif root.val == subRoot.val:
            return isSameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)








































        '''#Attempt 2
        if not root:
            return False
        # Check if the trees match at the current node
        if self.isSameTree(root, subRoot):
            return True
        # Otherwise, check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:  
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        # Check left and right children
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)'''














        
        
        
        
        
        
        #Attempt 1
        '''if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def sameTree(self,r,q):
        if not r and not q:
            return True
        if not r or not q:
            return False
        if r.val != q.val:
            return False
        return self.sameTree(r.left,q.left) and self.sameTree(r.right,q.right)'''

        
        
        
