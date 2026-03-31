class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Attempt 3
        #What makes a valid tree? I think no cycles. is it valid if there disconnected components? Can the input be null? 
        #Brute Force - Go thru each node individually and ensure no cycles 
        #Optimal - Create and adj list and dfs to detect cycles and disconnects with a visit set
        #complexities brute: 0(n!)? and space 0(1) and optimal 0(2(V+E)) time and O(V+E) Space since memoization of visit allows not revisiting

        adj = {i: [] for i in range(n)}
        for idx0,idx1 in edges:
            adj[idx0].append(idx1)
            adj[idx1].append(idx0)
        path=[]
        #detect cycle
        def dfs(vertice,visit,prev):
            #base case
            if vertice in path:
                return False
            path.append(vertice)
            for i in adj[vertice]:
                if i!=prev:
                    if not dfs(i,path,vertice):
                        return False

            return True
        
        #
        if not dfs(0,path,None):
            return False
        elif len(path)<n:
            return False
        return True






























        
        #Attempt 2
        '''if len(edges) != n-1:
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
        return dfs(0,-1) and len(visit)==n'''
        
        
        
        
        #Attempt 1
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