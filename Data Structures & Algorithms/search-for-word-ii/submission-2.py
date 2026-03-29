class TrieNode:
    def __init__(self):
        self.chars = {}
        self.word = None  # stores full word at end node

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        
        # build trie
        for word in words:
            node = root
            for char in word:
                if char not in node.chars:
                    node.chars[char] = TrieNode()
                node = node.chars[char]
            node.word = word  # mark end with the word itself
        
        rows, cols = len(board), len(board[0])
        res = []

        def dfs(node, i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            char = board[i][j]
            if char == '#' or char not in node.chars:
                return
            next_node = node.chars[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # avoid duplicates
            board[i][j] = '#'
            dfs(next_node, i+1, j)
            dfs(next_node, i-1, j)
            dfs(next_node, i, j+1)
            dfs(next_node, i, j-1)
            board[i][j] = char

        for i in range(rows):
            for j in range(cols):
                dfs(root, i, j)
        
        return res