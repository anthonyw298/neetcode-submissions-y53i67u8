class MedianFinder:
    def __init__(self):
        self.lst=[]
    def addNum(self, num: int) -> None:
        self.lst+=[num]
        self.lst=sorted(self.lst)
    def findMedian(self) -> float:
        if len(self.lst)%2==1:
            return self.lst[(len(self.lst)//2)]
        else:
            return (self.lst[(len(self.lst)//2)]+self.lst[(len(self.lst)//2)-1])/2
        
        