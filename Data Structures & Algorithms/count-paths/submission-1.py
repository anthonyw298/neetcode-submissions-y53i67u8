class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = dp[max(i - 1,0)][j] + dp[i][max(0,j-1)]
        return dp[m-1][n-1]

        















































        '''dp=[1]*n
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j]+=dp[j+1]
        return dp[0]'''
        

        