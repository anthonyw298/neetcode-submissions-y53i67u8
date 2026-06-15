class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if i >= n or j >= m:
                return 0
            if cache[i][j] != -1:  # already computed, return it
                return cache[i][j]
            if text1[i] == text2[j]:
                cache[i][j] = dfs(i + 1, j + 1) + 1
            else:
                cache[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return cache[i][j]

        return dfs(0, 0)





































        '''
        #optimized
        row = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            newRow = [0] * (len(text2) + 1)
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    newRow[j] = row[j - 1] + 1
                else:
                    newRow[j] = max(row[j], newRow[j - 1])
            row = newRow
        return row[len(text2)]'''























        #bottom up
        '''dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[len(text2)][len(text1)]'''

























        #top down
        '''dp = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            elif (i,j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                dp[(i,j)] = dfs(i + 1, j + 1) + 1
            else:
                dp[(i,j)] = max(dfs(i, j + 1), dfs(i + 1, j))
            return dp[(i,j)]
        return dfs(0,0)'''