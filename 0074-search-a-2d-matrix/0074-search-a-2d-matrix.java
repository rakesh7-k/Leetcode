class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int low=0;
        int high=matrix[0].length*matrix.length-1;
        int r=matrix.length;
        int c=matrix[0].length;
        if(r==0|| c==0 ) return false;
        while(low<=high){
            int mid=low+(high-low)/2;
            int val= matrix[mid/c][mid%c];
            if (val==target){
                return true;
            }
            else if(val<target){
                low=mid+1;
            }
            else{
                high=mid-1;
            }
        }
        return false;
    }
}