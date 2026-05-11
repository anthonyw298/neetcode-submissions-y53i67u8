class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        satisfied = 0
        res = ''
        l = 0
        for r in range(len(s)):
            have[s[r]] += 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                satisfied += 1
            while satisfied == len(need):
                if len(res) == 0 or r - l + 1 < len(res):
                    res = s[l : r + 1]
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    satisfied -= 1
                l += 1
        return res






































        '''seenT = Counter(t)
        seenS = {}
        have = 0
        need = len(seenT)
        res = ''
        resLen = float('inf')
        l = 0
        for r in range(len(s)):
            seenS[s[r]] = seenS.get(s[r], 0) + 1
            if seenS[s[r]] == seenT[s[r]]:
                have += 1
            while have == need:
                if r -  l + 1 < resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                seenS[s[l]] -= 1
                if s[l] in seenT and seenS[s[l]] < seenT[s[l]]:
                    have -= 1
                l += 1
        return res'''










































        
        '''#Attempt 2
        l,res,have,need,cnt,minL=0,'',{},{},0,float('infinity')
        for i in t:
            need[i]=1+need.get(i,0)
        print(len(need))
        for r in range(len(s)):
            have[s[r]]=1+have.get(s[r],0)
            if s[r] in need:
                if have[s[r]]==1 and cnt==0:
                    l=r
                if have[s[r]]==need[s[r]]:
                    print('hi')
                    cnt+=1
            if cnt==len(need):
                print(have)
                if minL>len(s[l:r]):
                    res=s[l:r+1]
                    minL=r-l+2
                    print(minL,'minl')
                    while cnt==len(need):
                        print('bru')
                        have[s[l]] = have.get(s[l], 0) - 1
                        if s[l] in need:
                            if have[s[l]]<need[s[l]]:
                                print(have[s[l]],need[s[l]],s[l])
                                if have[s[l]]<=0:
                                    print('bruh')
                                    have.pop(s[l])
                                cnt-=1
                        l+=1
        return res'''

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''Looking at Solution to Understand
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

        return res if resLen != float("infinity") else ""'''
