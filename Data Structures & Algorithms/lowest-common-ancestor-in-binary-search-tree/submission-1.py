# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Attempt 2
        if not root:
            return
        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root
















        
        #Attempt 1
        '''if not root:
            return False
        if self.TorF(root,p,q):
            return root
        else:
            return self.lowestCommonAncestor(root.left,p,q) or self.lowestCommonAncestor(root.right,p,q)
    def TorF(self,root,l,r):
        if root.left and root.right:
            if l.val in {root.val,root.left.val,root.right.val}:
                if r.val in {root.val,root.left.val,root.right.val}:
                    return True
        return False'''