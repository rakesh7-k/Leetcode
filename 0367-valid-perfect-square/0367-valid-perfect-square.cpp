class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num == 1)
        return true;

        for(int i = 1; ; i++){
            double k = (double)num / (double)i;
            if(i == k)
            return true;
            else if(k < i)
            return false;
        }
        return false;
    }
};