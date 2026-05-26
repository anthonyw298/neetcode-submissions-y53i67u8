class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memoisation table: (row, col) -> number of paths from that cell to the goal
        dp: dict[tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            # out of bounds → no path
            if i >= m or j >= n:
                return 0
            # reached the destination → exactly one path (stay here)
            if i == m - 1 and j == n - 1:
                return 1
            # already computed this cell?
            if (i, j) in dp:
                return dp[(i, j)]

            # move right and down, add the results
            ways = dfs(i + 1, j) + dfs(i, j + 1)

            # memo‑store the result before returning
            dp[(i, j)] = ways
            return ways

        # start from the top‑left corner (0,0)
        return dfs(0, 0)