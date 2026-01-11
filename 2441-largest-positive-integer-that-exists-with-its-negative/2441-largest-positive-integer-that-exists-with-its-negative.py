class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=[]
        b=[]
        for i in nums:
            if i <0:
                a.append(abs(i))
            b.append(i)
        a.sort()
        b.sort()
        for i in a[::-1]:
            if i in b[::-1]:
                return i
        return -1

        
            
        