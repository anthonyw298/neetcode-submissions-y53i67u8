class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
            if j >= len(t):
                return 1
            elif i >= len(s):
                return 0
            elif (i, j) in cache:
                return cache[(i,j)]
            match = s[i] == t[j]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j) 
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]
        return dfs(0,0)
        # s = xxyxy, t = xy
        #         ^
        # dic = {0:x, 2:y} -> {}
        # dic = {1:x} -> {1:x} -> {}
        # dic = {3:x} -> {3:x}
        # dict = {4:y} -> {4:y} -> {}
        # xSet = {0,1,3} -> {1,3} -> {3}
        # ySet = {2,4} -> {4} -> {}

        # 02 -> 



































        '''
        dp = {}

        def dfs(i, j):
            if j >= len(t):
                return 1
            elif i >= len(s):
                return 0
            elif (i,j) in dp:
                return dp[(i,j)]
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i + 1, j) + dfs(i + 1, j + 1)
            else:
                dp[(i,j)] = dfs(i + 1, j)
            return dp[(i, j)]
        return dfs(0,0)
        '''