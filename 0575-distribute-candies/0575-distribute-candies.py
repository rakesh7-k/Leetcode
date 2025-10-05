class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy=len(set(candyType))
        return min(candy,len(candyType)//2)
        

        