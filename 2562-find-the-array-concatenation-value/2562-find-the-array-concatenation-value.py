class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n=len(nums)
        a=[]
        if n%2!=0:
            a.append(nums[n//2])
        
        i=0
        j=n-1
        while i <j:
            k=str(nums[i])+str(nums[j])
            a.append(int(k))
            i+=1
            j-=1
        
        return sum(a)