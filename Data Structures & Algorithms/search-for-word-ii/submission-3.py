class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None  # store full word

class Solution:
    def findWords(self, board, words):
        # Build Trie
        root = Node()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
            node.end = True
            node.word = word  # store word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            char = board[i][j]

            if char not in node.children:
                return

            node = node.children[char]

            # 🎯 Found a word
            if node.word:
                res.append(node.word)
                node.word = None  # avoid duplicates

            # mark visited
            board[i][j] = "#"

# down
            if i + 1 < ROWS and board[i + 1][j] != "#":
                dfs(i + 1, j, node)

# up
            if i - 1 >= 0 and board[i - 1][j] != "#":
                dfs(i - 1, j, node)

# right
            if j + 1 < COLS and board[i][j + 1] != "#":
                dfs(i, j + 1, node)

# left
            if j - 1 >= 0 and board[i][j - 1] != "#":
                dfs(i, j - 1, node)
            # restore cell
            board[i][j] = char

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)

        return res

        
        
        
        
        
        
        
        
























        #Attempt 1
        '''res=[]
        sub=None
        rows,columns=len(board),len(board[0])
        def dfs(i,j,word,p):
            if p == len(word):
                return True
            if i>=rows or i<0 or j>=columns or j<0 or word[p] != board[i][j] or board[i][j] == '#':
                return False
            board[i][j] = '#'
            sub = dfs(i+1,j,word,p+1) or dfs(i,j+1,word,p+1) or dfs(i-1,j,word,p+1) or dfs(i,j-1,word,p+1)
            board[i][j] = word[p]
            return sub
        for i in range(len(words)):
            word=words[i]
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if dfs(x,y,word,0):
                        res+=[word]
        return list(set(res))'''