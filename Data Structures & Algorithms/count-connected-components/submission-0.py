class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Attempt 1
        res=0
        visit=set()
        adj={i:[] for i in range(n)}
        for p,c in edges:
            adj[p].append(c)
            adj[c].append(p)
        def dfs(i,prev):
            if i in visit:
                return
            visit.add(i)
            for j in adj[i]:
                if j==prev:
                    continue
                dfs(j,i)
        for i in adj:
            if i in visit:
                continue
            else:
                res+=1
                dfs(i,-1)
        return res

        
        