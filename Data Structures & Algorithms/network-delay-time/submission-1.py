class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for start, end, time in times:
            adjList[start].append((end,time))
        visit = set()
        heap = []
        heapq.heappush(heap,(0,k))
        maxSeen = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visit:
                continue
            maxSeen = max(maxSeen, dist)
            visit.add(node)
            for neighbor, weight in adjList[node]:
                heapq.heappush(heap, (dist + weight, neighbor))
        if len(visit) == n:
            return maxSeen
        return -1
