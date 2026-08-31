class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            sig = [0] * 26
            for char in word:
                sig[ord(char) - ord('a')] += 1
            if tuple(sig) in anagram:
                anagram[tuple(sig)].append(word)
            else:
                anagram[(tuple(sig))] = [word]
        return list(anagram.values())
