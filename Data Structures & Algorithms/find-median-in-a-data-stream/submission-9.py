class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.maxHeap and  -self.maxHeap[0] > num:
            heapq.heappush(self.maxHeap,-num)
        else:
            heapq.heappush(self.minHeap,num)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            num = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -num)

            

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]

        
        