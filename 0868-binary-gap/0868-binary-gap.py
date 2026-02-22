class Solution:
    def binaryGap(self, n: int) -> int:
        a=bin(n)[2:]
        a=list(a)
        i=0
        m=0
        while i<len(a):
            if a[i]=='1':
                j=i+1
                while j<len(a):
                    if a[j]=='1':
                        m = max(m, j - i)   
                        break
                        
                    j+=1
                    
            i+=1
        return m

        