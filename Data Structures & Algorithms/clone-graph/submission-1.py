"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Attempt 3
        #Questions - Undirected Graph Were Creating? Will there be multiple CC?
        #Brute Force - Not Really Clear maybe going thru each node and then making neighbors from adjList?
        #Optimal Version - Run DFS  starting at 1 until n using adjList to go thru its neighbors and backtrack if multiple 
        #Complexities - Brute Force : O(n^2) and 0(n) Optimal  - O(n) dfs and O(n) stack
        visit = {}
            

        def dfs(node):
            #We dont want to run into cycles
            if not node:
                return
            if node in visit:
                return visit[node]
            clone = Node()
            clone.val = node.val
            visit[node] = clone
            for i in node.neighbors:
                clone.neighbors.append(dfs(i))
            return dfs(node)
        return dfs(node)
























        #Attempt 2
        '''OldtoNew={}
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
        return dfs(node)'''

        #Attempt 1
        '''from collections import deque
        if not node:
            return
        queue=deque([node])
        while queue:
            root=queue.popleft()
            for node in root.neighbors:
                queue.append(node)'''