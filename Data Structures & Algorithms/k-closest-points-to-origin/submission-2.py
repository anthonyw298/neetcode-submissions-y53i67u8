class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = ((x**2) + (y**2)) ** .5
            heapq.heappush(heap, (-distance,x,y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            distance, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res














































        
        '''import heapq
        heap = []
        res = []
        for x, y in points:
            heapq.heappush(heap,(-(x**2 + y**2),[x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            num, coord = heapq.heappop(heap)
            res.append(coord)
        return res'''
