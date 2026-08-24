# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, high):
            nonlocal count
            if not node:
                return
            if high <= node.val:
                count += 1
            high = max(node.val, high)
            dfs(node.left, high)
            dfs(node.right, high)
            return 
        dfs(root, root.val) 
        return count