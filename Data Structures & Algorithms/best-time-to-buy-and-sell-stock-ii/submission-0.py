class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            elif (i, buy) in dp:
                return dp[(i, buy)]
            if buy:
                take = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, buy)
                dp[(i, buy)] = max(take, skip)
            else:
                sell = dfs(i + 1, True) + prices[i]
                skip = dfs(i + 1, False)
                dp[(i, buy)] = max(sell, skip)
            return dp[(i, buy)]
        return dfs(0, True)