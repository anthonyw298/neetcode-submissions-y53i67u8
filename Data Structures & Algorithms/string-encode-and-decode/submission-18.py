class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            length = len(word)
            res.append(str(length))
            res.append('#')
            res.append(word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        length = 0
        while i < len(s):
            if s[i] == '#':
                res.append(s[i + 1: i + length + 1])
                i = i + length + 1
                length = 0
            elif s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1
        return res

            
            
