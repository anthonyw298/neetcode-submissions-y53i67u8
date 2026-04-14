class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1,n):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[i].append([dist,j])
                adjList[j].append([dist,i])
        res = 0
        minH = [[0,0]]
        visit = set()
        while len(visit) < n:
            cost , point = heapq.heappop(minH)
            if point in visit:
                continue
            visit.add(point)
            res += cost
            for neiCost,nei in adjList[point]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])
        return res

