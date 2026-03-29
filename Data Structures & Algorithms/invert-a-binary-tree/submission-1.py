# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            #Attempt 3-Stack
            if not root:
                return
            stack=[root]
            while stack:
                node=stack.pop()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                node.left,node.right=node.right,node.left
            return root


            #Attempt 2-BFS
            '''from collections import deque
            if not root:
                return
            queue=([root])
            while queue:
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)'''


            #Attempt 1-DFS
            '''if not root:
                return
            else:
                rootL=self.invertTree(root.left)
                rootR=self.invertTree(root.right)
                root.left,root.right=rootR,rootL
                return root'''