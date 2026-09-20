class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei != prev and not dfs(nei, node):
                    return False
            return True
        if not dfs(0,0):
            return False
        return len(visit) == n