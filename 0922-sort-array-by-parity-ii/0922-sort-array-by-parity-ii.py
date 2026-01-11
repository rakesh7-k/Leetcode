class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        evencnt=0
        odcnt=0
        res=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else :
                odd.append(i)
        even.sort()
        odd.sort()
        for i in range(len(nums)):
            if i%2!=0:
                res.append(odd[odcnt])
                odcnt+=1
            elif i%2==0:
                res.append(even[evencnt])
                evencnt+=1
        return res


        