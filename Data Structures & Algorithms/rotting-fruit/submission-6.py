class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            i, j, time = queue.popleft()
            if i + 1 < rows and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                queue.append((i + 1, j, time + 1))
            if j + 1 < cols and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                queue.append((i, j + 1, time + 1))
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                queue.append((i - 1, j, time + 1))
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                queue.append((i, j - 1, time + 1))
            res = max(res, time)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res

