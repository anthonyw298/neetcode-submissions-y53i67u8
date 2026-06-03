class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1]
        right = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right.append(right[-1] + 1)
            else:
                right.append(1)
        right.reverse()
        res = 0
        for i in range(len(left)):
            res += max(left[i],right[i])
        return res