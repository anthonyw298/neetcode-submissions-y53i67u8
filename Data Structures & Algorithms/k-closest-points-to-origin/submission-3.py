class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (x**2 + y**2)** .5
        heap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = ((x**2 + y**2))**.5
            heapq.heappush(heap,(-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res