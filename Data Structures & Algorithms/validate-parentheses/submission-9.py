class Solution:
    def isValid(self, s: str) -> bool:
        #Attempt 2 - Brute
        dic = {"(":')',"{":'}',"[":"]"}
        stack = []
        if len(s)==0:
            return False
        for i in s:
            print(i)
            if i in dic:
                stack.append(i)
            elif i in dic.values():
                if len(stack)==0:
                    return False
                elif dic[stack[-1]]==i:
                    print(dic[stack[-1]],i)
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack==[]:
            return True
        return False

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''if len(s)%2==1:
            return False
        stack=[]
        for i in range(len(s)):
            if s[i] in {'(',"[","{"}:
                stack.append(s[i])
            elif s[i] in {')','}',']'} and len(stack)==0:
                return False
            else:
                if (stack[-1]=='(' and s[i]==')') or (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']'):
                    stack.pop()
                else: 
                    return False
        print(stack)
        if not stack:
            return True
        return False'''
