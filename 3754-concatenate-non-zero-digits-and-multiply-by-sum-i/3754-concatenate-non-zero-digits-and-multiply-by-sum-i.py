class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if  n==0:
            return 0
        s=str(n)
        total=0
        a=[]
        for i in s:
            if i!='0':
                a.append(i)
                total+=int(i)
        
        res=''.join(a)
        return int(res)*total
        