class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visit=set()
        adj={i:[] for i in range(n)}
        for p,c in edges:
            adj[p].append(c)
            adj[c].append(p)
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n
        
        
        
        
        
        '''adjList = {i: [] for i in range(n)}
        visit=set()
        for p,c in edges:
            adjList[p].append(c)
        def dfs(i):
            if i+1==n:
                return True
            if i in visit:
                return False
            visit.add(i)
            for j in adjList[i]:
                if not dfs(j):
                    return False
                visit.remove(i)
            return True

        return dfs(0)'''