class Solution {
    public int singleNumber(int[] nums) {
      int inn=0;
      for(int i=0;i<nums.length;i++)  
{
    inn=inn^nums[i];

}
return inn;
}
}