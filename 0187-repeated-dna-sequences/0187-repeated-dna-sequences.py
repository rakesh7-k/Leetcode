class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen,res=set(),set()
        for l in range(len(s)-9):
            curr=s[l:l+10]
            if curr in seen:
                res.add(curr)
            else:
                seen.add(curr)
        return list(res)
        