class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp, rows, cols = {}, len(matrix), len(matrix[0]) 
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 0
            elif (i,j) in dp:
                return dp[(i, j)]
            down = dfs(i + 1,j) if i + 1 < rows and matrix[i + 1][j] > matrix[i][j] else 0
            up = dfs(i - 1, j) if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j] else 0
            right = dfs(i, j + 1) if j + 1 < cols and matrix[i][j + 1] > matrix[i][j] else 0
            left = dfs(i, j - 1) if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j] else 0
            dp[(i,j)] = max(left,right,up,down) + 1
            return dp[(i, j)]
        for i in range(rows):
            for j in range(cols):
                dfs(i,j)
        return max(dp.values())
        