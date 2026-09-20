class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visit = set()
        def dfs(crs):
            if adj[crs] == []:
                return True
            elif crs in visit:
                return False
            visit.add(crs)
            print(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            adj[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True