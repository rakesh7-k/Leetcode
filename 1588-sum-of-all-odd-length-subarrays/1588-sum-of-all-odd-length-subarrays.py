
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i, n):
                sub = arr[i:j+1]
                if len(sub) % 2 == 1:
                    total += sum(sub)
                    
        return total