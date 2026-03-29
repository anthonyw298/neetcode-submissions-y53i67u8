class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache={len(s):True}
        def dfs(i):
            if i in cache:
                return cache[i]
            for w in wordDict:
                if ((i+len(w)) <= len(s) and s[i:i+len(w)] == w):
                    if dfs(i+len(w)):
                        cache[i]=True
                        return True
            cache[i]=False
            return False
                        
        return dfs(0)
        
        #Attempt 1
        #dfs - iterate thru until in wordDict 
            #base case is if currstring is not none and len s is none false else true
            #recurse & run thru until base case to return true or false
        #other matches same thing
        cache={len(s):1}
        def dfs(i):
            #true base case
            if i in cache:
                return True
                
            
        
        
        
            






        