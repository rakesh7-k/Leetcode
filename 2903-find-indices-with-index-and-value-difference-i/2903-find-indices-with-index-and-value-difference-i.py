class Solution:
    def findIndices(self, nums: List[int], id: int, vd: int) -> List[int]:
        i=0
        j=1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(i-j)>=id and abs(nums[i]-nums[j])>=vd:
                    return [i,j]            
            
                
        return [-1,-1]
        