# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            elif self.isSameTree(node, subRoot):
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right
        return dfs(root)
    def isSameTree(self, p, q):
        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val:
                return False
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return left and right
        return dfs(p, q)