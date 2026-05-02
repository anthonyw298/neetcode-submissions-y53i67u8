class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # prices[i] = cheapest cost to reach node i
        prices = [float('inf')] * n
        prices[src] = 0

        # relax edges k+1 times (k stops = k+1 edges)
        for i in range(k + 1):
            # snapshot prices before this round — critical!
            # prevents using edges added in the SAME round
            temp = prices.copy()

            for begin, end, cost in flights:
                if prices[begin] == float('inf'):
                    continue  # can't reach begin yet, skip
                # can we reach `end` cheaper through `begin`?
                if prices[begin] + cost < temp[end]:
                    temp[end] = prices[begin] + cost

            prices = temp  # commit this round's updates

        return prices[dst] if prices[dst] != float('inf') else -1









































        '''prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]'''














































        '''prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            copy = prices.copy()
            for start,stop,cost in flights:
                if copy[start] != float('inf'):
                    if cost + copy[start] < prices[stop]:
                        prices[stop] = cost + copy[start]
        return prices[dst] if prices[dst] != float('inf') else -1'''
