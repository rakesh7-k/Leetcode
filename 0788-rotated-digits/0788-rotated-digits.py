class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic={2:5,
            5:2,
            6:9,
            9:6}
        c=0
        for num in range(1,n+1):
            s=str(num)
            new=""
            valid=True
            for d in s:
                if int(d) in {3,4,7}:
                    valid=False
                    break
                if int(d) in dic:
                    new+=str(dic[int(d)])
                else:
                    
                    new+=d
            if valid:
                new=int(new)
                if new!=num:
                    c+=1
        return c


        