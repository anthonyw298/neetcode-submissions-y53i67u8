class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, a):
            if i >= len(coins) or a > amount:
                return 0
            elif a == amount:
                return 1
            elif (i, a) in dp:
                return dp[(i, a)]
            take = dfs(i, a + coins[i])
            skip = dfs(i + 1, a)
            dp[(i, a)] = take + skip
            return dp[(i, a)]
        return dfs(0, 0)





































        '''
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = dp[i - coin] +dp[i]
        return dp[amount]'''

