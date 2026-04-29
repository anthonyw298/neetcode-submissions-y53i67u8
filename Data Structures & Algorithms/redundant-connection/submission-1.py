class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0] * (len(edges) + 1)
        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return [x, y]
            elif rank[px] < rank[py]:
                parent[px] = py
            elif rank[py] < rank[px]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] = rank[py] + 1
            return
        for x,y in edges:
            tmp = union(x, y)
            if tmp:
                return tmp
        

        















































        '''n = len(edges)
        parent = list(range(n+1))
        rank = [0] * (n + 1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            px, py = find(x), find(y)
            if px == py:# this is a cycle?
                return True
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1

            return False

        for x,y in edges:
            if union(x,y):
                return [x,y]'''
