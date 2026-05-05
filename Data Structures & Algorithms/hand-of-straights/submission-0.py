class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        hand.sort()
        while sum(freq.values()) > 0:
            start = min(freq)
            for j in range(groupSize):
                if start + j not in freq or freq[start + j] == 0:
                    return False
                freq[start + j] -= 1
                if freq[start + j] == 0:
                    del freq[start + j]
        return True
                
