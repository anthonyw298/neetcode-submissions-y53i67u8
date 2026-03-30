class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Attempt 2
        #Not Really Sure About Brute Force
        #DFS Backtracking with Memoization
        #O(mn* 4^(mn)) & 0(n*m)
        res=0
        ROWS,COLS = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>=ROWS or j<0 or j>=COLS or grid[i][j]=='0' or grid[i][j]=='#':
                return 
            grid[i][j]='#'
            dfs(i+1,j) 
            dfs(i,j+1) 
            dfs(i-1,j) 
            dfs(i,j-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1':
                    dfs(i,j)
                    print(grid)
                    res+=1
        return res

        
































        #Attempt 1
        '''visited=set()
        islands=0
        def dfs(i,j):
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or (i,j) in visited or grid[i][j]=='0':
                return
            visited.add((i,j))
            print(i,j,'in',visited)
            return dfs(i+1,j) or dfs(i,j+1) or dfs(i-1,j) or dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and grid[i][j] == '1': 
                    islands+=1
                    print(i,j,'out')
                    dfs(i,j)
                else:
                    visited.add((i,j))
        return islands'''