class Solution {
public:
    int maxProduct(int n) {
        int arr[1001];
        int x=0,m=-243,t,sm=0;
        while(n>0){
            t=n%10;
            
            if (t>m){
                sm=m;
                m=t;
            }
            else if(t>sm) sm=t;
            n/=10;
        }
    
    return sm*m;
    }
};