# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([])
        queue.append((root,0))
        res = []
        while queue:
            root, i = queue.popleft()
            if i >= len(res):
                res.append([])
            res[i].append(root.val)
            if root.left:
                queue.append((root.left, i + 1))
            if root.right:
                queue.append((root.right, i + 1))
        return res
            
        