class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=''
        for word in strs:
            print(word,'word')
            for char in word:
                print(char,'char')
                encode+=str(ord(char))
                encode+=" "
                print(encode,'encode')
            encode+=','
        print(encode)
        return encode
    def decode(self, s: str) -> List[str]:
        print(s,'decode stage')
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


        return decode