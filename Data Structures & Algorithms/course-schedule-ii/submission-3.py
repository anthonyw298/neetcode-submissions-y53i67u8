class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        output, cycle = [], set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in output:
                return True
            cycle.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            output.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
            
            


