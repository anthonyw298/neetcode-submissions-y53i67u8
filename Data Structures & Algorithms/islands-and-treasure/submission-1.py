class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        bfs = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs.append((i, j, 0))
        while bfs:
            i, j, dist = bfs.popleft()
            if i + 1 < rows and grid[i + 1][j] == 2147483647:
                bfs.append((i + 1, j, dist + 1))
                grid[i + 1][j] = dist + 1
            if i - 1 >= 0 and grid[i - 1][j] == 2147483647:
                bfs.append((i - 1, j, dist + 1))
                grid[i - 1][j] = dist + 1
            if j + 1 < cols and grid[i][j + 1] == 2147483647:
                bfs.append((i, j + 1, dist + 1))
                grid[i][j + 1] = dist + 1
            if j - 1 >= 0 and grid[i][j - 1] == 2147483647:
                bfs.append((i, j - 1, dist + 1))
                grid[i][j - 1] = dist + 1





































        
        '''
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            i, j = queue.popleft()
            if i+1 < rows and grid[i+1][j] == 2147483647:
                queue.append((i+1, j))
                grid[i+1][j] = grid[i][j] + 1
            if i-1 >= 0 and grid[i-1][j] == 2147483647:
                queue.append((i-1, j))
                grid[i-1][j] = grid[i][j] + 1
            if j+1 < cols and grid[i][j+1] == 2147483647:
                queue.append((i, j+1))
                grid[i][j+1] = grid[i][j] + 1
            if j-1 >= 0 and grid[i][j-1] == 2147483647:
                queue.append((i, j-1))
                grid[i][j-1] = grid[i][j] + 1'''

                