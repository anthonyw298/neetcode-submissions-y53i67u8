class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for _ in range(n)]
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                cols.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = 'Q'
                dfs(r + 1)
                cols.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                board[r][c] = '.'
            return
        dfs(0)
        return res

            
                
