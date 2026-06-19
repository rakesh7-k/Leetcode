class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        w=0
        for i in range(0,len(gain)):
            w=w+gain[i]
            a.append(w)
        return max(a)
            
        