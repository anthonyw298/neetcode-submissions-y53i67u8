class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #not sure how to reverse all diagonals
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()

        




        