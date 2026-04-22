class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]
        l, r = 0, len(lst) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp > lst[mid][1]:
                l = mid + 1
            elif timestamp < lst[mid][1]:
                r = mid - 1
            else:
                return lst[mid][0]
        return lst[r][0] if r >= 0 else ""

        
