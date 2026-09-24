class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            summ=0
            s=str(nums[i])
            for j in s:
                summ+=int(j)
            if summ==i:
                return i

        
        return -1

        