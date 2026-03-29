# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Attempt 2
        return self.check(root,float('-inf'),float('inf'))
    def check(self,root,low,high):
        if not root:
            return True
        if not (low<root.val<high):
            return False
        return self.check(root.left,low,root.val) and self.check(root.right,root.val,high)
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''if not root:
            return False 
        while root.left or root.right:
            if not root.left and not root.right:
                return True
            elif not root.right:
                if root.left.val<root.val:
                    return self.isValidBST(root.left)
                else:
                    return False
            elif not root.left:
                if root.right.val>root.val:
                    return self.isValidBST(root.right)
                else:
                    return False
            elif root.left.val<root.val and root.right.val>root.val:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False
        return True'''
        
