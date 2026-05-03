class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if coin > i:
                    continue
                else:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

            
    
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]





















































        '''#Attempt 2
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1) 
        return dp[amount] if dp[amount] != amount + 1 else -1'''


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        #remainder : [num-1,num-5,num-10]
        '''cache={}
        def dfs(amount):
            if amount==0:
                return 0
            if amount in cache:
                return cache[i]
            
            
        return dfs(amount)'''
        