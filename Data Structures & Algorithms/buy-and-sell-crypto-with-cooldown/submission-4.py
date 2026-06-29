class Solution:
    def maxProfit(self, prices):
        dp = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            elif (i, buy) in dp:
                return dp[(i,buy)]
            if buy:
                take = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                dp[(i,buy)] = max(take, skip)
            else:
                sell = dfs(i + 2, True) + prices[i]
                skip = dfs(i + 1, False)
                dp[(i,buy)] = max(sell, skip)
            return dp[(i, buy)]
        return dfs(0, True)





































        '''
        #space optimized
        dpS = 0
        dpB1 = 0
        dpB2 = 0
        for i in range(len(prices) - 1, -1, -1):
            tmp = dpB1
            dpB1 = max(-prices[i] + dpS, dpB1)
            dpS = max(dpB2 + prices[i], dpS)
            dpB2 = tmp
        return dpB1'''























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


