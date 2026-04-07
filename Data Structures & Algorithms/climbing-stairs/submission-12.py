class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2
        if n==1:
            return one
        elif n==2:
            return two
        for i in range(2,n):
            temp = one
            one = two
            two = temp + two
        return two





































        '''#Attempt-Bottom Up
        cache=[-1]*(n+1)
        cache[0]=1
        cache[1]=1
        for i in range(2,n+1):
            cache[i]=cache[i-1]+cache[i-2]
        print(cache)
        return cache[n]'''

        #Attempt-Top Down
        '''cache=[-1]*(n+1)
        def dfs(i):
            if i<=1:
                return 1
            if cache[i] != -1:
                return cache[i]
            else:
                cache[i]=dfs(i-1)+dfs(i-2)
            return cache[i]
        return dfs(n)'''
        #Attempt-Pointer Optimal
        '''one,two = 1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one'''
        #Attempt 1
        '''if n<=0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 3
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)'''