# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.most = 0
        self.dfs(root)
        return self.most
    def dfs(self, node):
        if not node:
            return 0 
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.most = max(self.most, left + right)
        return max(left,right) + 1







































        '''def maxDiameter(root):
            if not root:
                return 0
            left = maxDiameter(root.left)
            right = maxDiameter(root.right)
            self.most = max(self.most,left+right)
            return max(left,right) + 1
        self.most = 0
        maxDiameter(root)
        return self.most'''







































        '''self.most = 0
        def dfs(node):
            if not node:
                return 0
            leftH = dfs(node.left)
            rightH = dfs(node.right) 
            d = leftH + rightH
            self.most = max(self.most, d)
            return max(leftH,rightH) + 1
        dfs(root)
        return self.most '''