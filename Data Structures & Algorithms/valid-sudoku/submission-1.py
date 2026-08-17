class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]  # row[i] = digits seen in row i
        col = [set() for _ in range(9)]  # col[j] = digits seen in col j
        box = [set() for _ in range(9)]  # box[k] = digits seen in 3x3 box k

        for i in range(9):          # i = row index
            for j in range(9):      # j = col index
                val = board[i][j]
                if val == '.':      # skip empty cells
                    continue

                box_idx = (i // 3) * 3 + (j // 3)  # maps (i,j) to one of 9 boxes

                if val in row[i] or val in col[j] or val in box[box_idx]:
                    return False    # duplicate found in row, col, or box

                row[i].add(val)
                col[j].add(val)
                box[box_idx].add(val)

        return True