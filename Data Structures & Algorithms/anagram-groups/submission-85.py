class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sig = [0] * 26
            for char in word:
                sig[ord(char)-ord('a')] += 1
            res[tuple(sig)].append(word)
        return list(res.values())






































        '''
        #Attempt 4
        res=[]
        anagrams=defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(string)
        for key,value in anagrams.items():
            res.append(value)
        return res'''

            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 3
        '''dic={}
        for string in strs:
            sig=[0]*26
            for char in string:
                sig[ord(char)-ord('a')]+=1
            sig=tuple(sig)
            if sig in dic:
                dic[sig]+=[string]
            else:
                dic[sig]=[string]
        print(dic)
        return list(dic.values())'''
            


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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


























                