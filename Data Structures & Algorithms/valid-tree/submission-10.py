class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges and n > 0:
            return True
        adjList = {i : [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visit = set()
        def dfs(c, prev):
            if c in visit:
                return False
            if adjList[c] == []:
                return True
            visit.add(c)
            for d in adjList[c]:
                if d == prev:
                    continue
                if not dfs(d, c):
                    return False
            adjList[c] == []
            return True

        if not dfs(0, None):
            return False
        if len(visit) < len(adjList):
            return False
        return True