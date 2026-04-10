class Solution:
    def numDecodings(self, s: str) -> int:  
        #Attempt 3
        dp = {}
        dp[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            dp[i] = 0
            if s[i] != '0':
                dp[i] = dp[i+1]
            if i<len(s)-1:
                if s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'):
                    dp[i] += dp[i+2] 
        return dp[0]












































        #Attempt 2
        '''cache = {len(s):1}
        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i]=='0':
                return 0
            res = dfs(i+1)
            if i+1<len(s) and (s[i]=='1' or s[i] == '2' and s[i+1] in '0123456'):
                res += dfs(i+2)
            cache[i]=res
            return res
        return dfs(0)'''
              
        #Attempt 1
        '''if s[0]=='0':
            return 0
        res=0
        alpha={}
        for i in range(26):
            alpha[chr(ord('A') + i)]=str(i+1)
        print(alpha)
        l,r=0,1
        for i in s:
            print(i,s[l:r])
            if s[l:r] in alpha.values():
                print('a')
                r+=1
                res+=1
            else:
                print('b')
                l+=1
                print(l,r)
                if s[l:r] in alpha.values() and l<r-1:
                    res+=1
                

        return res'''

