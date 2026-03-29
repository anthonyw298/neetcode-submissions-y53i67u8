class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big={}
        lst=[]
        cnt=0
        keyz=None
        keyy=None
        for i in strs:
            small={}
            for j in i:
                if j in small:
                    small[j]+=1
                else:
                    small[j]=1
            for key,value in big.items():
                if small==value:
                    cnt=1
                    keyz=i
                    keyy=key
                    print('keyy',keyy)
            if cnt != 1:
                big[i]=small
                lst+=[[i]]
            else:
                for x in lst:
                    if x[0]==keyy:
                        x+=[keyz]
                        keyz=None
                        keyy=None
                        cnt=0

        print(big)
        print(lst)
        return lst