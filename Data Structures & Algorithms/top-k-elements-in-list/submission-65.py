class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        res = []
        for key,val in freq.items():
            heapq.heappush(heap,(val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            val, key = heapq.heappop(heap)
            res.append(key)
        return res