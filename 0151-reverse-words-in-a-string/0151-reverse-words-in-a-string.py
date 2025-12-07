class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        a=[]
        for i in range(len(word)-1,-1,-1):
            a.append(word[i])
            if i!=0:
                a.append(" ")
        return "".join(a)
        