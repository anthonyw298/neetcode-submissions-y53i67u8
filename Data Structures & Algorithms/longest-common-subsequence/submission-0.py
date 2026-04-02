class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in cache:          # need to check cache
                return cache[(i, j)]
            if text1[i] == text2[j]:
                res = 1 + dfs(i+1, j+1) # missing assignment
            else:
                res = max(dfs(i+1, j), dfs(i, j+1)) # missing assignment
            cache[(i, j)] = res          # cache the (i,j) pair, not the chars
            return res                   # missing return
        return dfs(0, 0)                 # missing return