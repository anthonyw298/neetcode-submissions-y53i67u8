class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i : [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visit = set()
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for j in adjList[i]:
                dfs(j)
            adjList[i] == []
            return
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res