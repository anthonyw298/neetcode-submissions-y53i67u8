class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxLen = 0
        rows,cols = len(grid) , len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] == '#' or grid[i][j] == 0:
                return 0
            grid[i][j] = '#'
            return dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1) + 1
        for i in range(rows):
            for j in range(cols):
                maxLen = max(maxLen, dfs(i,j))
        return maxLen