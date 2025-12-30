class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=0
        ans=1
        maxx=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                ans+=1
            else:
                maxx=max(maxx,ans)
                ans=1
                
        return max(maxx,ans)

        