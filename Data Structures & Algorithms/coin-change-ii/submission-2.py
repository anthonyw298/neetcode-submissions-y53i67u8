class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #bottom up
        row = [0] * (amount + 1)
        row[0] = 1
        for i in range(len(coins)):
            nextRow = [0] * (amount + 1)
            nextRow[0] = 1
            for j in range(1, amount + 1):
                nextRow[j] = row[j]
                if j - coins[i] >= 0:
                    nextRow[j] += nextRow[j - coins[i]]
            row = nextRow 
        return row[amount]
















        #top down
        '''dp = {}
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

        return dfs(0, amount)'''