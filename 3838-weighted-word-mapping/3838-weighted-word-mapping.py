class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=[]
        s=[]
        for i in words:
            n=0
            for j in i:
                n+=weights[(ord(j)-97)%26]
            res.append(n)
        for i in res:
            n=i%26
            f=abs(n-26)
            s.append(chr(f+96))
        return ''.join(s) 


        