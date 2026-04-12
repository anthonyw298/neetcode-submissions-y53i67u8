class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            copy = prices.copy()
            for start,stop,cost in flights:
                if copy[start] != float('inf'):
                    if cost + copy[start] < prices[stop]:
                        prices[stop] = cost + copy[start]
        return prices[dst] if prices[dst] != float('inf') else -1
