class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        for start in sorted(freq):
            count = freq[start]
            if count > 0:
                for i in range(groupSize):
                    if not freq[start + i] or freq[start + i] < count:
                        return False
                    freq[start + i] -= count
        return True