class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        n, ans = len(nums), inf
        nums.sort()

        for left, rght in zip(nums[:n//2], nums[n-1: n//2-1: -1]):
            ans = min(ans, left + rght)
            
        return ans/2    