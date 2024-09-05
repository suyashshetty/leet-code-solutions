package algorithms.arrays.LeetCode31;

/**
 * LeetCode Problem 31
 * Level: Medium
 * Title: Next Permutation
 * 
 * Description:
 * Implement next permutation, which rearranges numbers into the 
 * lexicographically next greater permutation of numbers. If such 
 * an arrangement is not possible, it must rearrange it as the 
 * lowest possible order (i.e., sorted in ascending order). The 
 * replacement must be in-place and use only constant extra memory.
 * 
 * Example:
 * Input: [1,2,3]
 * Output: [1,3,2]
 */
public class LeetCode31 {

    /**
     * Rearranges numbers into the lexicographically next greater permutation.
     * 
     * @param nums the input array of numbers
     */
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;

        // Step 1 : Find first decreasing element
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        // Step 2: Find element to swap with if step 1 is found
        if (i >= 0) {
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }

        // Step 3: Reverse the sequence from i + 1 to end
        reverse(nums, i + 1, n - 1);
    }

    /**
     * Swaps two elements in the array.
     * 
     * @param nums the array of numbers
     * @param i    index of the first element
     * @param j    index of the second element
     */
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    /**
     * Reverses the elements in the array from start to end.
     * 
     * @param nums  the array of numbers
     * @param start the starting index
     * @param end   the ending index
     */
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
}
