class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i : [] for i in range(1, n + 1)}
        for s, d, w in times:
            adjList[s].append((d, w))
        t = 0
        visit = set()
        heap = [(0, k)]
        while heap:
            w1, d1 = heapq.heappop(heap)
            if d1 in visit:
                continue
            visit.add(d1)
            t = max(t, w1)
            for d2, w2 in adjList[d1]:
                heapq.heappush(heap,(w2 + w1, d2))
        return t if len(visit) == n else -1
            

        