class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()
        def dfs(r,c,visit):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'X' or board[r][c] == 'T' or (r,c) in visit:
                return
            visit.add((r,c))
            board[r][c] = 'T'
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)

        
        for r in range(rows):
            dfs(r,0,visit)
            dfs(r,cols - 1,visit)
        for c in range(cols):
            dfs(0,c,visit)
            dfs(rows-1,c,visit)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
