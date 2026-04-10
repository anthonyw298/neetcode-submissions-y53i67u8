class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # min possible unmatched '('
        high = 0  # max possible unmatched '('

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1   # treat '*' as ')'
                high += 1  # treat '*' as '('
        
            if high < 0:      # too many ')' in best case
                return False
            low = max(low, 0) # can't go below 0

        return low == 0

        