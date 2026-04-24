# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root):
        if not root:
            return '#'
        self.res = []
        self.dfss(root)
        return "#".join(self.res)
    def dfss(self, root):
        if not root:
            self.res.append('N')
        else:
            self.res.append(str(root.val))
            self.dfss(root.left)
            self.dfss(root.right)
    












































    '''res=[]
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)'''

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    '''res = []

        def dfs(node):
            if not node:
                res.append("X")
                return
        
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)'''
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        if data == '#':
            return 
        data = data.split('#')
        self.queue = deque(data)
        return self.dfs()
    def dfs(self):
        if not self.queue:
            return
        val = self.queue.popleft()
        if val == 'N':
            return
        node = TreeNode(int(val))
        node.left = self.dfs()
        node.right = self.dfs()
        return node
        

        
        
















































    '''vals=data.split(",")
        self.i=0
        def dfs():
            if vals[self.i]=='N':
                self.i+=1
                return
            node=TreeNode(int(vals[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node

        return dfs()'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    '''vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "X":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()'''



        
