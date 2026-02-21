import math
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt=0
        s=0
        def is_prime(n):
            if n <= 1: return False
            if n == 2: return True
            if n % 2 == 0: return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0: return False
            return True
        for i in range(left,right+1):
            a=bin(i)[2:]
            a=list(a)
            s = sum(int(x) for x in a)            
            if is_prime(s):
                cnt+=1
        return cnt
            
            

                