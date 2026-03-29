"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Attempt 2
        OldtoNew={}
        def dfs(node):
            if not node:
                return 
            if node in OldtoNew:
                return OldtoNew[node]
            copy = Node(node.val)
            OldtoNew[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node)

        #Attempt 1
        '''from collections import deque
        if not node:
            return
        queue=deque([node])
        while queue:
            root=queue.popleft()
            for node in root.neighbors:
                queue.append(node)'''