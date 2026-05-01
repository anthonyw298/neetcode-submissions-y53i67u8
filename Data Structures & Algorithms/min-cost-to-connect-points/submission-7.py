class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i,len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        heap = []
        visit = set()
        heapq.heappush(heap, [0,0])
        res = 0
        while heap:
                cost, i = heapq.heappop(heap)
                if i in visit:
                    continue
                visit.add(i)
                for neiCost, nei in adj[i]:
                    if nei not in visit:
                        heapq.heappush(heap,[neiCost,nei])
                res += cost
        return res
                

                





































        '''heap = [(0, 0)]
        visit = set()
        res = 0
        while heap:
            cost, i = heapq.heappop(heap)
            if i in visit:
                continue
            visit.add(i)
            res += cost
            x1, y1 = points[i]
            for j in range(len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(heap,(dist,j))
        return res'''

            