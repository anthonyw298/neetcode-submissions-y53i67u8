class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            sig = [0] * 26
            for char in word:
                sig[ord(char) - ord('a')] += 1
            if tuple(sig) not in dic:
                dic[tuple(sig)] = []
            dic[tuple(sig)].append(word)
        return list(dic.values())
                