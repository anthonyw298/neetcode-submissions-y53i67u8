class TreeNode:
    def __init__(self,val=None,children=None,end=False):
        self.val=val
        self.children=children if children is not None else {}
        self.end=end

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
        return True