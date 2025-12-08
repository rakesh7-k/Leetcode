class Solution {
    public boolean judgeCircle(String m) {
        int x=0,y=0;
     for (char i: m.toCharArray()){
        if(i=='U')x++;
        else if(i=='D')x--;
        else if (i=='R') y++;
        else if (i=='L') y--;
       
     }   
      return x==0&&y==0;
    }
}