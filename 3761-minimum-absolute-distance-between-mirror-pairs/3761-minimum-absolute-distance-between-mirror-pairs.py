class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        last_seen = {}
        min_dist = float('inf')

        for i, val in enumerate(nums):
            if val in last_seen:
                min_dist = min(min_dist, i - last_seen[val])
            
            mirror = int(str(val)[::-1])
            last_seen[mirror] = i
            
        return min_dist if min_dist != float('inf') else -1
