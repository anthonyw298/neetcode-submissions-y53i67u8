class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                    grid[i][j] = 2
        time = 0
        while queue:
            i, j, time = queue.popleft()
            if i + 1 < rows and grid[i + 1][j] == 1:
                queue.append((i + 1, j, time + 1))
                grid[i + 1][j] = 2
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                queue.append((i - 1, j, time + 1))
                grid[i - 1][j] = 2
            if j + 1 < cols and grid[i][j + 1] == 1:
                queue.append((i, j + 1, time + 1))
                grid[i][j + 1] = 2
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                queue.append((i, j - 1, time + 1))
                grid[i][j - 1] = 2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return time
        
            
                    





































        '''rows, cols, queue, res = len(grid), len(grid[0]), deque([]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            i, j, lvl = queue.popleft()
            res = max(res,lvl)
            if i+1 < rows and grid[i+1][j] == 1:
                queue.append((i+1,j,lvl+1))
                grid[i+1][j] = grid[i][j]
            if i-1 >= 0 and grid[i-1][j] == 1:
                queue.append((i-1,j,lvl+1))
                grid[i-1][j] = grid[i][j]
            if j+1 < cols and grid[i][j+1] == 1:
                queue.append((i,j+1,lvl+1))
                grid[i][j+1] = grid[i][j]
            if j-1 >= 0 and grid[i][j-1] == 1:
                queue.append((i,j-1,lvl+1))
                grid[i][j-1] = grid[i][j]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res'''
            

    















































'''def orangesRotting(self, grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Load ALL rotten oranges as sources simultaneously
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    time = 0
    directions = [[0,1],[0,-1],[1,0],[-1,0]]

    while queue:
        r, c, t = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, t + 1))
                time = t + 1

    return time if fresh == 0 else -1'''