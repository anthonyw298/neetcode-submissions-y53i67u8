class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #top down with cache
        dp = {}
        def dfs(i,j):
            if i <= 0  or j <= 0:
                return 1
            elif (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = dfs(i - 1, j) + dfs(i, j - 1) 
            return dp[(i,j)]
        return dfs(m - 1,n - 1)


























        #bottom up
        '''dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]'''

        















































        '''dp=[1]*n
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j]+=dp[j+1]
        return dp[0]'''
        

        