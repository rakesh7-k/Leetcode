class Solution:
    def mirrorDistance(self, n: int) -> int:
        sn=str(n)[::-1]
        return abs(int(sn)-n)
        