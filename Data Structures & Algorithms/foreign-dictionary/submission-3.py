class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Attempt 2
        adj = {i:set() for word in words for i in word}
        for i in range(len(words)-1):
            c=words[i]
            n=words[i+1]
            minLen=min(len(c),len(n))
            if len(c)>len(n) and c[:minLen] == n[:minLen]:
                return ""
            for i in range(minLen):
                if c[i] != n[i]:
                    adj[c[i]].add(n[i])
                    break
        visit={}
        res=[]
        def dfs(char):
            if char in visit:
                return visit[char]

            visit[char]=True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            visit[char]=False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
        print(adj)















        
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
            
        
        