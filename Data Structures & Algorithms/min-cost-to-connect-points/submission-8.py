class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i : [] for i in range(n)}
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                d = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((d, j))
                adjList[j].append((d, i))
        visit = set()
        heap = [(0, 0)]
        res = 0
        while len(visit) < n:
            d1, i1 = heapq.heappop(heap)
            if i1 in visit:
                continue
            visit.add(i1)
            res += d1
            for d2, i2 in adjList[i1]:
                heapq.heappush(heap,(d2,i2))
        return res
