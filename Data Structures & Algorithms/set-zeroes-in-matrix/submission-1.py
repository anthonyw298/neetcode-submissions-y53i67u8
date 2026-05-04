class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        colZero = False
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            if matrix[i][0] == 0:
                colZero = True

        for j in range(cols):
            if matrix[0][j] == 0:
                rowZero = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        if rowZero:
            for j in range(cols):
                matrix[0][j] = 0

        if colZero:
            for i in range(rows):
                matrix[i][0] = 0
        














































        '''ROWS,COLS=len(matrix),len(matrix[0])
        rowZero=False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c]==0:
                    matrix[0][c] = 0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        rowZero = True
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        if matrix[0][0]==0:
            for r in range(ROWS):
                matrix[r][0]=0
        if rowZero:
            for c in range(COLS):
                matrix[0][c]=0'''
        