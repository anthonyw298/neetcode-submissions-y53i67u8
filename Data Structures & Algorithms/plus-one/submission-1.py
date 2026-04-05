class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        pointer=1
        newNum=digits[0]+1
        lead=newNum//10
        digits[0]=newNum%10
        while lead==1 and pointer<len(digits):
            newNum=digits[pointer]+1
            lead=newNum//10
            digits[pointer]=newNum%10
            pointer+=1
        if lead==1:
            digits.append(1)
        digits.reverse()
        return digits
        

        
            

        