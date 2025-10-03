class Solution {
    public void nextPermutation(int[] nums) {
        // Step 1: Find the pivot (first number from end where nums[i-1] < nums[i])
        // Example: nums = [1,2,3,6,5,4]
        // i starts at 5 (index of 4), nums[i-1]=5 >= nums[i]=4 → move left
        // nums[3]=6 >= nums[4]=5 → move left
        // nums[2]=3 < nums[3]=6 → pivot found at i-1=2
        int i = nums.length - 1;
        while (i > 0 && nums[i-1] >= nums[i]) {
            i--;
        }

        // If no pivot is found, the array is descending → reverse the whole array
        if (i == 0) {
            reverse(nums, 0, nums.length-1);
            return;
        }

        // Step 2: Find the number just bigger than pivot to swap
        // Pivot = nums[2] = 3
        // Start from end: nums[5]=4 > 3 → swap pivot with 4
        int j = nums.length - 1;
        while (j >= i && nums[j] <= nums[i-1]) {
            j--;
        }

        swap(nums, i-1, j); // nums becomes [1,2,4,6,5,3]

        // Step 3: Reverse the suffix after pivot
        // Reverse nums[3..5] = [6,5,3] → [3,5,6]
        // Final array: [1,2,4,3,5,6] → next permutation
        reverse(nums, i, nums.length-1);
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
