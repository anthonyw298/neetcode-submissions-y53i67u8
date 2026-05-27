class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        buy = [0] * (n + 2)
        sell = [0] * (n + 2)
    
        for i in range(n - 1, -1, -1):
            buy[i] = max(-prices[i] + sell[i + 1], buy[i + 1])
            sell[i] = max(prices[i] + buy[i + 2], sell[i + 1])
    
        return buy[0]























        #top down 
        '''if len(prices) == 1:
            return 0
        dp = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            elif (i, buy) in dp:
                return dp[(i,buy)]
            elif buy:
                dp[(i,buy)] = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                dp[(i,buy)] = max(prices[i] + dfs(i + 2, True), dfs(i + 1, False))
            return dp[(i,buy)]
        return dfs(0, True)'''


