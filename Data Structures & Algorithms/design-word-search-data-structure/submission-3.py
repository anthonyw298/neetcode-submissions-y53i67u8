class TrieNode():
    def __init__(self):
        self.chars={}
        self.end=False
    
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.chars:
                node.chars[char]=TrieNode()
            node=node.chars[char]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.end
            if word[i] == '.':
                for char in node.chars:
                    if dfs(node.chars[char],i+1):
                        return True
                return False
            elif word[i] in node.chars:
                if dfs(node.chars[word[i]],i+1):
                    return True
            return False

        return dfs(self.root,0)
        
