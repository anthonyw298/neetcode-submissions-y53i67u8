class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) 
        for s, d, t in times:
            adj[s].append((t, d))
        heap = [(0, k)]
        visit = set()
        t = 0
        while heap:
            d, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            t = d
            for d2, node2 in adj[node]:
                if node2 not in visit:
                    heapq.heappush(heap,(d2 + d, node2))
        print(visit, n)
        return t if len(visit) == n else -1

            









































        '''adjList = defaultdict(list)
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
        return -1'''
