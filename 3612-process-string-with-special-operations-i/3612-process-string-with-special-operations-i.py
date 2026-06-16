class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        for i in s:
            if i.isalpha():
                res.append(i)
            elif i=='*':
                if len(res)!=0:
                    res.pop(-1)
            elif i=='#':
                res=res*2
            elif i=='%':
                res=res[::-1]
        return ''.join(res)
        