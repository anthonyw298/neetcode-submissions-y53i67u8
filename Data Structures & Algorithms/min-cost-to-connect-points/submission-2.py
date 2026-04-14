class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minimum = [float('inf')] * n
        minimum[0] = 0
        res = 0
        # Step 1: Find cheapest unvisited point
        for _ in range(n):
            cheapest = -1
            for i in range(n):
                if i not in visited and (cheapest == -1 or minimum[i] < minimum[cheapest]):
                    cheapest = i
        # Step 2: Connect it
            visited.add(cheapest)
            res += minimum[cheapest]
         # Step 3: Update costs for unvisited points
            x1, y1 = points[cheapest]
            for i in range(n):
                if i not in visited:
                    x2, y2 = points[i]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    minimum[i] = min(minimum[i], dist)
        return res
