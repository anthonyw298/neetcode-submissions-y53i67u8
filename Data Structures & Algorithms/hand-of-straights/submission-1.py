class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        print(freq,sorted(freq))
        for start in sorted(freq):
            count = freq[start]
            if count > 0:
                for j in range(groupSize):
                    if freq[start + j] < count:
                        return False
                    freq[start + j] -= count
        return True