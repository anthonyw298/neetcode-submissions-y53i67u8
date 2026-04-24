class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heapq.heappush(heap,-num)
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            c = abs(a - b)
            heapq.heappush(heap,-c)
        res = heapq.heappop(heap)
        return -res

        