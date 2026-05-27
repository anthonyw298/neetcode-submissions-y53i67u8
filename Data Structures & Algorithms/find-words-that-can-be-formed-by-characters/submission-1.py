class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        total = 0
        for word in words:
            flag = True
            for char in word:
                if char in freq and freq[char] >= word.count(char):
                    continue
                else:
                    flag = False
                    break
            if flag:
                    total += len(word)

        return total
            