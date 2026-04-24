from collections import Counter
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        queue = deque([])
        for key in count:
            heapq.heappush(heap, (-count[key]))
        time = 0
        while heap or queue:
            if not heap:
                time = queue[0][0]
            if queue and queue[0][0] == time:
                temp = queue.popleft()
                heapq.heappush(heap,(temp[1]))
            time += 1
            freq = heapq.heappop(heap)
            freq += 1
            if freq < 0:
                queue.append([time + n, freq])
        return time
            