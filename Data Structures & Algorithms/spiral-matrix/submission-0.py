class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        res=[]

        while top <= bottom and left <= right:
            # go right along top
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # go down along right
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            if not (top <= bottom and left <= right):
                break
            # go left along bottom
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1

            # go up along left
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        return res





            #00-01-02-12-22-21-20-10-11
        '''tbl,tbr=0,len(matrix)-1
        res=[]
        i=j=0
        while len(res)<len(matrix)**2:
            res.append(matrix[i][j])
            if (i == 0  and j < tbr) or matrix[i-1][j] in res:
                j+=1
            if i < tbr and j < tbr:
                i+=1
            if i == tbr and j < tbr:
                j-=1
            if i == 0 and j < tbr:
                i-=1
        return res'''


