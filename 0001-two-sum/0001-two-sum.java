import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[][] pairs = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            pairs[i][0] = nums[i];
            pairs[i][1] = i;
        }
        
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));
        
        int low = 0;
        int high = n - 1;
        
        while (low < high) {
            int sum = pairs[low][0] + pairs[high][0];
            
            if (sum == target) {
                return new int[] { pairs[low][1], pairs[high][1] };
            } else if (sum < target) {
                low++;
            } else {
                high--;
            }
        }
        
        return new int[] {};
    }
}