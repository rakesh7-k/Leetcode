class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        cnt=0
        if num2<100 :
            return 0
        for i in range(num1,num2+1):
            i=str(i)
            n=len(i)
        
            for j in range(1,n-1):
                if int(i[j-1])<int(i[j]) and int(i[j+1])<int(i[j]) :
                    cnt+=1
                elif int(i[j-1])>int(i[j]) and int(i[j+1])>int(i[j]) :
                    cnt+=1
        return cnt


