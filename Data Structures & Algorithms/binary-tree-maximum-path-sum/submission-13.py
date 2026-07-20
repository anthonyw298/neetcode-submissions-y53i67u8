# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        final = root.val

        def dfs(node):
            nonlocal final
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            left = max(left, 0)    # ADDED: if a child's contribution is negative, don't include it
            right = max(right, 0)  # ADDED: same for right

            final = max(final, left + right + node.val)  # CHANGED: always consider the "bridge" case now
            return node.val + max(left, right)             # CHANGED: simplified return, no more if/else branching

        dfs(root)
        return final