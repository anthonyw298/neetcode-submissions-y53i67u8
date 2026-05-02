class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap,(grid[0][0], 0, 0)) #maxSeen,i,j
        visit = set()
        while heap:
            maxSeen, i, j = heapq.heappop(heap)
            if i == rows - 1 and j == cols - 1:
                return maxSeen
            if (i,j) in visit:
                continue
            visit.add((i,j))
            if i + 1 < rows and (i + 1, j) not in visit:
                heapq.heappush(heap,(max(maxSeen,grid[i + 1][j]), i + 1, j))
            if i - 1 >= 0 and (i - 1, j) not in visit:
                heapq.heappush(heap,(max(maxSeen,grid[i - 1][j]), i - 1, j))
            if j + 1 < cols and (i , j + 1) not in visit:
                heapq.heappush(heap,(max(maxSeen,grid[i][j + 1]), i, j + 1))
            if j - 1 >= 0 and (i, j - 1) not in visit:
                heapq.heappush(heap,(max(maxSeen,grid[i][j - 1]), i, j - 1))
        








































        
        '''rows, cols = len(grid), len(grid[0])
        heap = []
        visit = set()
        heapq.heappush(heap, (grid[0][0], 0, 0))  
        while heap:
            maxElev, i, j = heapq.heappop(heap)
            if (i,j) in visit:
                continue
            if i == rows - 1 and j == cols - 1:
                return maxElev
            visit.add((i,j))
            if i + 1 < rows and (i+1,j) not in visit:
                heapq.heappush(heap, (max(maxElev, grid[i+1][j]), i+1, j))  
            if j + 1 < cols and (i,j+1) not in visit:
                heapq.heappush(heap, (max(maxElev, grid[i][j+1]), i, j+1)) 
            if i - 1 >= 0 and (i-1,j) not in visit:
                heapq.heappush(heap, (max(maxElev, grid[i-1][j]), i-1, j)) 
            if j - 1 >= 0 and (i,j-1) not in visit:
                heapq.heappush(heap, (max(maxElev,grid[i][j-1]), i, j-1)) '''



