import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # maxHeap (store negatives)
        self.large = []  # minHeap

    def addNum(self, num: int) -> None:
        # Step 1: push into maxHeap
        heapq.heappush(self.small, -num)

        # Step 2: ensure ordering (maxHeap top <= minHeap top)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2