class Solution:
    def compress(self, chars: List[str]) -> int:
        r, w = 0, 0
        while r < len(chars):
            char = chars[r]
            count = 0
            while r < len(chars) and chars[r] == char:
                r += 1
                count += 1
            chars[w] = char
            w += 1
            if count > 1:
                count = str(count)
                for i in range(len(count)):
                    chars[w] = count[i]
                    w += 1
        return w