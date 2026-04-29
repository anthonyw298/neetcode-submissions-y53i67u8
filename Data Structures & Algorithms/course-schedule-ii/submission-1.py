class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList, queue, inDegree, res = {i : [] for i in range(numCourses)}, deque([]), [0] * numCourses, []
        
        for course, pre in prerequisites:
            adjList[pre].append(course)
            inDegree[course] += 1
        print(adjList)
        print(inDegree)
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            res.append(course)
            for nei in adjList[course]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        if len(res) == numCourses:
            return res
        return []
        














































        '''from collections import deque,defaultdict
        res = []
        adjList = defaultdict(list)
        inDegree = [0] * numCourses
        #Build the Graph
        for course, pre in prerequisites:
            adjList[pre].append(course)
            inDegree[course] += 1
        #Seed the Queue
        queue = deque([])
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        #BFS Loop
        while queue:
            pre = queue.popleft()
            res.append(pre)
            for course in adjList[pre]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        return res if len(res) == numCourses else []'''

        