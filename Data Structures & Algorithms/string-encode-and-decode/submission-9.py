class Solution:

    def encode(self, strs: List[str]) -> str:
        #Attempt 2
        lst=[]
        for string in strs:
            lst+=[str(len(string)),'#']
            for char in string:
                lst+=[char]
        return "".join(lst)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''encode=''
        for word in strs:
            print(word,'word')
            for char in word:
                print(char,'char')
                encode+=str(ord(char))
                encode+=" "
                print(encode,'encode')
            encode+=','
        print(encode)
        return encode'''
    def decode(self, s: str) -> List[str]:
        #Attempt 2
        print(s,len(s))
        r=0
        l=0
        res=[]
        while r<len(s):
            while s[r]!="#":
                r+=1
            length=int(s[l:r])
            print(length,r,l)
            res+=[s[r+1:r+length+1]]
            r+=length+1
            print(r)
            l=r
        return res

            








        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''print(s,'decode stage')
        decode=[]
        letter=''
        word=''
        for char in s:
            if char==",":
                decode+=[word]
                word=""
            elif char ==" ":
                word+=str(chr(int(letter)))
                print(word)
                letter=""
            else:       
                letter+=str(char)
        return decode'''