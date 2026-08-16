class Solution {
    public void swap(int[] arr,int i,int j){
        int t=arr[i];
        arr[i]=arr[j];
        arr[j]=t;
        
    }
    public void sortColors(int[] nums) {
        int mid=0;
        int low=0;
        int high=nums.length-1;
        while(mid<=high){
            if (nums[mid]==0){
                swap(nums,low,mid);
                mid++;
                low++;
            }
            else if (nums[mid]==1) mid++;
            else{
                swap(nums,high,mid);
                high--;
            }
        }

    }
}