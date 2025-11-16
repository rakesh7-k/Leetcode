class Solution:
    def numSub(self, s: str) -> int:
        res=0
        mod=10**9+7
        consecutive=0
        for i in s:
            if i=='1':
                consecutive+=1
                res=(res+consecutive)%mod
            else:
                consecutive=0
        return  res
        