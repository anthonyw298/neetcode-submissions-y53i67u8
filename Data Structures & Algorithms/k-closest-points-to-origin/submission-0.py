class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from math import sqrt
        heap = []
        res = []
        for x, y in points:
            heapq.heappush(heap,(-(sqrt((x)**2 + (y)**2)),[x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            num, coord = heapq.heappop(heap)
            res.append(coord)
        return res
