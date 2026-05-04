class CountSquares:

    def __init__(self):
        self.pcount = defaultdict(int)
        self.point = []

    def add(self, point: List[int]) -> None:
        self.pcount[tuple(point)] += 1
        self.point.append(point)
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.point:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            res += self.pcount[(px,y)] * self.pcount[(x,py)]
        return res
            

        
