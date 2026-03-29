class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Attempt 1
        '''Looking at Solution to Understand'''
        ws,wt={},{}
        for c in t:
            wt[c]=1+wt.get(c,0)
        l,res,resLen,have,need=0,'',float('infinity'),0,len(wt)
        for r in range(len(s)):
            # add
            ws[s[r]]=1+ws.get(s[r],0)
            #if its freq are equal then have+=1
            if s[r] in wt and ws[s[r]]==wt[s[r]]:
                have+=1
            #while have==need:
            while have==need:
                #l+=1 and remove from windows
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                ws[s[l]]-=1
                if s[l] in wt and ws[s[l]] < wt[s[l]]:
                    have-=1
                l+=1
                
            #check with res adn update reslen

        return res if resLen != float("infinity") else ""
