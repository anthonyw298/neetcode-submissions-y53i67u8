class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        heap = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    heapq.heappush(heap,(0,i, j))
        while heap:
            time, i, j = heapq.heappop(heap)
            if grid[i][j] != 2147483647 and grid[i][j] != 0:
                continue
            grid[i][j] = time
            time += 1
            if i + 1 < rows and grid[i + 1][j] == 2147483647:
                heapq.heappush(heap,(time, i + 1, j))
            if i - 1 >= 0 and grid[i - 1][j] == 2147483647:
                heapq.heappush(heap,(time, i - 1, j))
            if j + 1 < cols and grid[i][j + 1] == 2147483647:
                heapq.heappush(heap,(time, i, j + 1))
            if j - 1 >= 0 and grid[i][j - 1] == 2147483647:
                heapq.heappush(heap,(time, i , j - 1))
        return


