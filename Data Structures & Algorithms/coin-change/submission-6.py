class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(i, remain):
            if i >= len(coins) or remain < 0:
                return float('inf')
            elif remain == 0:
                return 0
            elif (i, remain) in dp:
                return dp[(i, remain)]
            dp[(i, remain)] = min(dfs(i, remain - coins[i]) + 1, dfs(i + 1, remain)) 
            return dp[(i, remain)]

        return -1 if dfs(0, amount) == float('inf') else dfs(0, amount)