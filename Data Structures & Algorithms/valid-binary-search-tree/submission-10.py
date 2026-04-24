# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         return self.valid(root, float('inf'),float('-inf'))

    def valid(self, root, maxSeen, minSeen):
        if not root:
            return True
        elif root.val >= maxSeen or root.val <= minSeen:
            return False
        return self.valid(root.left, min(maxSeen, root.val), minSeen) and self.valid(root.right, maxSeen, max(minSeen, root.val))







































        '''#Attempt 4

        def valid(root,Min,Max):
            if not root:
                return True
            if root.val>=Max or root.val<=Min:
                return False
            return valid(root.left,Min,root.val) and valid(root.right,root.val,Max)
            

        return valid(root,float('-inf'),float('inf'))'''






























        '''#Attempt 3

        def range(root,small,large):
            if not root:
                return True
            if root.val>=large or root.val<=small:
                return False
            return range(root.left,small,root.val) and range(root.right,root.val,large)
        return range(root,float('-infinity'),float('infinity')) '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''return self.check(root,float('-inf'),float('inf'))
    def check(self,root,low,high):
        if not root:
            return True
        if not (low<root.val<high):
            return False
        return self.check(root.left,low,root.val) and self.check(root.right,root.val,high)'''
        
        
        
        
        
        
        
        
        
        
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
        
