class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        ecnt,ocnt=0,0
        o=0
        e=0
        for i in range(1,2*n):
            if i%2!=0 and ocnt<=n:
                o+=i
                ocnt+=1
            elif i%2==0 and ecnt<=n :
                e+=i
                ecnt+=1
        a=o
        b=e
        while b!=0:
            a,b=b,a%b
        return a
        