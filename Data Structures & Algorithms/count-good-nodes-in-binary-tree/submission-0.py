# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, high):
            if not root:
                return 0 
            elif not high:
                return dfs(root.left, root.val) + dfs(root.right, root.val)
            elif root.val < high:
                return dfs(root.left, max(root.val,high)) + dfs(root.right, max(high,root.val))
            else:
                return dfs(root.left, max(root.val, high)) + dfs(root.right, max(root.val, high)) + 1

        return dfs(root, None) + 1
