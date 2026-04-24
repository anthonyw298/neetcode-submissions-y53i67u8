# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, queue = [], deque([])
        queue.append((root, 0))
        while queue:
            node, lvl = queue.popleft()
            if lvl >= len(res):
                res.append(node.val)
            if node.right:
                queue.append((node.right, lvl + 1))
            if node.left:
                queue.append((node.left, lvl + 1))
        return res