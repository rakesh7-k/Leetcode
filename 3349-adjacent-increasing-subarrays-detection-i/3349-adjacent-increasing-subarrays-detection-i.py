class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        inc=1
        pi=0
        maxlen=0
        for i  in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1
            else:
                pi=inc
                inc=1
            maxlen=max(maxlen,max(inc>>1,min(pi,inc)))
            if maxlen>=k:
                return True
        return False
        