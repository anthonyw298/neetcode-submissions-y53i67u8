class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
        #Attempt 1
        '''visit=[]
        adj = {c: [] for word in words for c in word}

        for i in range(len(words) - 1):
            curr = words[i]
            nex = words[i + 1]
    
    # invalid case
            if len(curr) > len(nex) and curr.startswith(nex):
                return ""
    
            for j in range(min(len(curr), len(nex))):
                if curr[j] != nex[j]:
                    adj[curr[j]].append(nex[j])
                    break
        print(adj)
        def dfs(char):
            print(char)
            if char in visit:
                return 
            visit.append(char)
            for i in adj[char]:
                dfs(i)
            return
        dfs(next(iter(adj)))
        return ''.join(visit)'''
            
        
        