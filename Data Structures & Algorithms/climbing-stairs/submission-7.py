class Solution:
    def climbStairs(self, n: int) -> int:
        #Attempt 2
        one,two = 1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one
        #Attempt 1
        if n<=0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 3
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)