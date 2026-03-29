class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1
        #Attempt 1
        #remainder : [num-1,num-5,num-10]
        '''cache={}
        def dfs(amount):
            if amount==0:
                return 0
            if amount in cache:
                return cache[i]
            
            
        return dfs(amount)'''
        