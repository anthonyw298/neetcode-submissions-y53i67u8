class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]













































        '''import heapq

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)  # remove smallest, keep k largest
        return heap[0]  # root is kth largest'''