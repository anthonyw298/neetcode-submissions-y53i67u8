class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]
        visit = set()
        res = 0
        while heap:
            cost, i = heapq.heappop(heap)
            if i in visit:
                continue
            visit.add(i)
            res += cost
            for j in range(len(points)):
                if j not in visit:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(heap, (dist, j))
        return res