class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Attempt 2
        l,res= 0,0
        for r in range(1,len(prices)):
            print(l,r)
            if prices[l]-prices[r]>0:
                l=r
            else:
                res=max(res,prices[r]-prices[l])
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''r=0
        l=0
        res=0
        while r<len(prices):
            print(r,l)
            #if its negative then l=r
            if prices[r]-prices[l]<=0:
                l=r
            else:
                if res<=prices[r]-prices[l]:
                    res=prices[r]-prices[l]
            r+=1
        return res'''