class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b=bin(n)[2:]
        s=''
        for i in b:
            if i=='0':
                s+='1'
            else:
               s+='0'
       
        return int(s,2)