class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        minn=min(a,b)
        cnt=0
        for i in range(1,minn+1):
            if a%i==0 and b%i==0:
                cnt+=1
        return cnt
        