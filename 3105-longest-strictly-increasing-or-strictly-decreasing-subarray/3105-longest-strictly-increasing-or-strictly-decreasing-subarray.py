class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc,dec,maxx=1,1,1
        for i in range(1,len(nums)):
            prev=nums[i-1]
            curr=nums[i]
            if prev>curr:
                dec+=1
                maxx=max(dec,maxx)
            else:
                dec=1
            if curr>prev:
                inc+=1
                maxx=max(maxx,inc)
            else:
                inc=1
        return maxx
            

        