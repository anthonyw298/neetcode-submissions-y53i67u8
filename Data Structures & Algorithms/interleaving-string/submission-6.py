class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def dfs(i,j):
            if i >= len(s1) and j >= len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = (i < len(s1) and dfs(i + 1,j) and s3[i + j] == s1[i] ) or (j < len(s2) and dfs(i,j + 1) and s3[i + j] == s2[j])

            return dp[(i,j)]
        return dfs(0,0)




































        '''
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0:
                    dp[i][j] |= dp[i-1][j] and s1[i-1] == s3[i+j-1]
                if j > 0:
                    dp[i][j] |= dp[i][j-1] and s2[j-1] == s3[i+j-1]
        
        return dp[len(s1)][len(s2)]'''

        
        