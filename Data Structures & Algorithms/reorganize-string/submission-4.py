class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s) #{a:3,b:2,c:1} - abaca
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""
        heap = []
        for key, value in freq.items():
            heapq.heappush(heap,(-value, key))
        prev = None
        res = []
        while heap:
            value, key = heapq.heappop(heap)
            res.append(key)
            value += 1
            if prev:
                heapq.heappush(heap, prev)
            if value < 0:
                prev = (value,key)
            else:
                prev = None
        return "".join(res)

        
        
