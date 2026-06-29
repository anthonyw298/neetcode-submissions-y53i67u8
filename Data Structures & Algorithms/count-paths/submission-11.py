class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            elif i == m or j == n:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = dfs(i, j + 1) + dfs(i + 1, j)
            return dp[(i, j)]
        return dfs(0, 0)




































        '''
        dp = {}
        def dfs(i, j):
            if i == m and j == n:
                return 1
            if i > m or j > n:
                return 0
            elif (i,j) in dp:
                return dp[(i,j)]
            else:
                dp[(i,j)] = dfs(i + 1,j) + dfs(i,j + 1) 
            return dp[(i,j)]
        return dfs(1,1)'''

            
            











































        '''
        cache = [[0] * n for _ in range(m)]
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            elif i >= m or j >= n:
                return 0
            elif cache[i][j] != 0:
                return cache[i][j]
            else:
                cache[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return cache[i][j]
        return dfs(0, 0)'''






































        '''
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(1, len(newRow)):
                newRow[j] = row[j] + newRow[j - 1]
            row = newRow
        return row[n - 1]'''




























        #top down with cache
        '''dp = {}
        def dfs(i,j):
            if i <= 0  or j <= 0:
                return 1
            elif (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = dfs(i - 1, j) + dfs(i, j - 1) 
            return dp[(i,j)]
        return dfs(m - 1,n - 1)'''


























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
        

        