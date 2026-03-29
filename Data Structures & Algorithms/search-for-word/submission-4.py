class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Attempt 3
        rows,columns=len(board),len(board[0])
        def dfs(i,j,cnt):
            #base case
            if cnt == len(word):
                return True 
            if i>=rows or i<0 or j>=columns or j<0 or board[i][j]!=word[cnt] or board[i][j]=='#':
                return False
            #append
            board[i][j]='#'
            #recurse
            res = dfs(i+1,j,cnt+1) or dfs(i,j+1,cnt+1) or dfs(i-1,j,cnt+1) or dfs(i,j-1,cnt+1)
            #undo
            board[i][j] = word[cnt]
            return res





        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
        




























        #Attempt 2
        '''res=None
        rows,columns=len(board),len(board[0])
        def dfs(i,j,p):
            print(i,j,p)
            if p==len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= columns or board[i][j] != word[p] or board[i][j] == '#':
                return False
            board[i][j]='#'
            res= dfs(i+1,j,p+1) or dfs(i,j+1,p+1) or dfs(i-1,j,p+1) or dfs(i,j-1,p+1)
            board[i][j]=word[p]
            return res
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i,j,0):
                    return True
        return False'''
























        #Attempt 1
        '''def dfs(i,j,curr,idx):
            print(curr)
            #base case
            if i>=len(board) or j>=i or j<0 or i<0:
                return
            if "".join(curr)==word:
                return True
            #include 
            if board[i][j]==word[idx]:
                curr.append(board[i])[j]
            #recursion
            else:
                curr.pop()
                idx-=1
            dfs(i+1,j,curr,idx+1)
            dfs(i,j+1,curr,idx+1)
            dfs(i-1,j,curr,idx+1)
            dfs(i,j-1,curr,idx+1)
                
            #exclude
        dfs(0,0,[],0)
        return False'''