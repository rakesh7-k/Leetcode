class Solution:
    def numSteps(self, s: str) -> int:
        a=int(s,2)
        cnt=0
        while a>1:

            if a%2!=0:
                a=a+1
            else:
                a=a//2
            cnt+=1
            
        return cnt
                

            

        