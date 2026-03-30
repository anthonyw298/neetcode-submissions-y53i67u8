class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Attempt 2
        #Questions - Can you walk me thru an example? Can we assume that the heights will contain atleast a 1x1 or more grid? Will there be negatives?
        #Brute - DFS without tracking the visited and starting from each index we would check its neighbors to be less until it reaches pacific and atlantic then mark it
        #Optimal - Create two sets for those that reach pacific, atlantic and then combine the two for both. top and left already in pacific so we can run dfs on rest same for atlantic. we can reverse by starting and making sure its going downwards (aka decreasing till edge)
        #Complexity - Brute : O(r*c^r*c) and space O(1) Optimal - Not Sure
        res=[]
        pac,atl=set(),set()

        def dfs(i,j,prev,ocean):
            #base case
            if i<0 or i>=len(heights) or j<0 or j>=len(heights[0]):
                return
            if heights[i][j]<prev or (i,j) in ocean:
                return
            num = heights[i][j]
            ocean.add((i,j))
            dfs(i+1,j,num,ocean)
            dfs(i,j+1,num,ocean)
            dfs(i-1,j,num,ocean)
            dfs(i,j-1,num,ocean)



        rows, cols = len(heights), len(heights[0])

        for j in range(cols):
            dfs(0, j, float('-inf'), pac)
            dfs(rows-1, j, float('-inf'), atl)

        for i in range(rows):
            dfs(i, 0, float('-inf'), pac)
            dfs(i, cols-1, float('-inf'), atl)
        for i in pac:
            if i in atl:
                res.append(list(i))    
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1 - After
        '''ROWS,COLS = len(heights),len(heights[0])
        pac,atl = set(),set()
        def dfs(r,c,visit,prevHeight):
            if r>=ROWS or c>=COLS or r<0 or c<0 or (r,c) in visit or prevHeight>heights[r][c]:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        res=[]
        for i in pac:
            if i in atl:
                res.append(i)
        return res'''
