class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #top down with cache
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

        















































        '''dp=[1]*n
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j]+=dp[j+1]
        return dp[0]'''
        

        