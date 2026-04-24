class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt=0
        r=0
        for i in moves:
            if i=='L':
                cnt-=1
            elif i=='R':
                cnt+=1
            else:
                r+=1
        return abs(cnt)+r
        