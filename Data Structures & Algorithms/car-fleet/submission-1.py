class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        fleets = 0
        prevTime = 0
        for pos, spd in pairs:
            time = (target - pos) / spd
            if time > prevTime:
                fleets += 1
                prevTime = time
        return fleets
