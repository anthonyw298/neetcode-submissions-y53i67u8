class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            elif i >= len(cost):
                return 0
            dp[i] = min(dfs(i + 1), dfs(i + 2)) + cost[i]
            return dp[i]
        return min(dfs(0), dfs(1))
























        '''res = float('inf')
        def dfs(i, count):
            if i >= len(cost):
                nonlocal res
                res = min(res,count)
                return
            dfs(i + 1, count + cost[i])
            dfs(i + 2, count + cost[i])
            return

        dfs(0, 0)
        dfs(1, 0)
        return res'''





































        '''one, two = 0, 0
        for i in range(2, len(cost) + 1):
            tmp = one
            one = min(one + cost[i-1], two + cost[i-2])
            two = tmp
        return one'''
        











































        


        '''dp = [float('inf')] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
        print(dp)
        return dp[len(dp) - 1]'''
