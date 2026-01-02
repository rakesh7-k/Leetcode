class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=stones
        while len(s)>1:
            x=max(s)
            s.remove(x)
            y=max(s)
            s.remove(y)
            if x!=y:
                s.append(abs(x-y))
        return s[0] if s else 0
            
        