class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Attempt 3
        dic={}
        for string in strs:
            sig=[0]*26
            for char in string:
                sig[ord(char)-ord('a')]+=1
            sig=tuple(sig)
            if sig not in dic:
                dic[sig]=[string]
            else:
                dic[sig]+=[string]
        print(dic)
        return list(dic.values())
            


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''dic={}
        if len(strs)<2:
            return [strs]

        for string in strs:
            signature=[0]*26
            for char in string:
                signature[ord(char)-ord('a')]+=1
            signature = tuple(signature)
            if signature not in dic:
                    dic[signature]=[string]
            else:
                    dic[signature]+=[string]
        return list(dic.values())'''
        
        #Attempt 1
        '''if len(strs)<2:
            return [strs]
        dic={}
        for i,string in enumerate(strs):
            count=[0]*26
            for j,char in enumerate(string):
                count[ord(char)-ord('a')]+=1
            print(count)'''


























                