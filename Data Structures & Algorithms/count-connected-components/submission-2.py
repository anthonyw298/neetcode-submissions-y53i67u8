class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Attempt 2
        #Question. could there be cycles? could there be multiple edges for a node? can n be 0? undirected
        #Brute Force would be to try all paths and see if multple paths and check if there is any that have completely different nodes in them entirely
        #Optimal - create adj list, run dfs. appends nodes for all valid paths in a connected component with a total counter
        #complexity - brute - 0((V+E)!) and 0(N) call stack but not sure why or can visualize. Optimal - O(V+E) time and space
        
        #Undirected Adj List
        adj={i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        total=0
        visit=set()
        def dfs(vertice,visit,prev):
            if vertice in visit:
                return
            visit.add(vertice)
            for i in adj[vertice]:
                if i != prev:
                    dfs(i,visit,vertice)
            return 

        for i in adj:
            if i not in visit:
                total+=1
            dfs(i,visit,None)
        return total
            

        






























        #Attempt 1
        '''res=0
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
        return res'''

        
        