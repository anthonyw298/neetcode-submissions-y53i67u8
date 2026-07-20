class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for course, pre in prerequisites:
            if course not in prereq:
                prereq[course] = []
            prereq[course].append(pre)
        visiting = set()   # nodes currently on the current DFS path (cycle detector)
        visited = set()    # nodes fully confirmed safe (no cycle through them)

        def dfs(course):
            if course in visiting:
                return False        # what should happen if we hit a node already on our current path?
            if course in visited:
                return True        # what should happen if we already know this course is safe?

            visiting.add(course)
            for pre in prereq.get(course, []):
                if not dfs(pre):
                    return False     # if a prerequisite fails, what happens to this course?

            visiting.remove(course)
            visited.add(course)
            return True            # what do we return if we got through the whole loop?  
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True