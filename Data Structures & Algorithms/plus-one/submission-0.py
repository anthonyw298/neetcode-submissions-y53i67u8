class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        num=digits[0]+1
        lead=num//10
        digits[0]=num%10
        i=1
        while lead!=0 and i<len(digits):
            num=digits[i]+lead
            lead=num//10
            digits[i]=num%10
            i+=1
        if lead==1:
            digits.append(1)
        digits.reverse()
        return digits
        