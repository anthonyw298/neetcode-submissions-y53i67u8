class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[: i] + '*' + word[i+1 :]
                dic[pattern].append(word)
        queue = deque([])
        visit = set(beginWord)
        queue.append(beginWord)
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                visit.add(word)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[: j] + '*' + word[j+1 :]
                    for nei in dic[pattern]:
                        if nei not in visit:
                            queue.append(nei)

            res += 1
        return 0