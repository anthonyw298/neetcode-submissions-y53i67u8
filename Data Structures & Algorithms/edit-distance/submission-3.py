class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i,j):
            #base case
            if j >= len(word2):
                return len(word1) - i 
            elif i >= len(word1):
                return len(word2) - j
            elif (i, j) in dp:
                return dp[(i, j)]
            match = word1[i] == word2[j]
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert = dfs(i, j + 1)
                delete = dfs(i + 1, j)
                replace = dfs(i + 1, j + 1)
                dp[(i, j)] = min(insert, delete, replace) + 1
            return dp[(i, j)]
        return dfs(0,0)