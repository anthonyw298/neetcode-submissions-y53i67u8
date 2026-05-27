class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, remain):
            if i >= len(coins) or remain < 0:
                return 0
            elif remain == 0:
                return 1
            elif (i,remain) in dp:
                return dp[(i, remain)]
            take = dfs(i, remain - coins[i]) 
            skip = dfs(i + 1, remain)
            dp[(i, remain)] = take + skip
            return dp[(i, remain)]

        return dfs(0, amount)