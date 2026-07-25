class Solution {
public:
    int maxProduct(int n) {
        int arr[1001];
        int x=0;
        while(n>0){
            arr[x++]=n%10;
            n/=10;
        }
    for(int i=0;i<x;i++){
          for(int j=0;j<x-i-1;j++){
            if( arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
          }
    }
    return arr[x-1]*arr[x-2];
    }
};