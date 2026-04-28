class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.end = True    
    def search(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end

    def startsWith(self,prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

















































'''class Node:
    def __init__(self):
        self.children={}
        self.end=False
class PrefixTree:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        #off
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]= Node()
            node=node.children[char]
        node.end=True
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.end:
            return True
        return False

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True'''































#Attempt 1
'''class TreeNode:
    def __init__(self):
        self.children={}
        self.end=False

class PrefixTree:
    def __init__(self):
        self.root=TreeNode()

    def insert(self, word: str) -> None:
        node = self.root              # no self.node
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()   # = not ==
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True'''