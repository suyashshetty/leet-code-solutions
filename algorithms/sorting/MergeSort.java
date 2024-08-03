package algorithms.sorting;

public class MergeSort {

    /**
     * Sorts the given array using merge sort.
     *
     * @param nums the array to sort
     * @return the sorted array, or the input array if it is null or empty
     */
    public int[] sort(int[] nums) {
        if (nums == null || nums.length == 0) {
            return nums; // Return the input as-is if it is null or empty
        }

        int[] temp = new int[nums.length]; // Temporary array for merging
        mergesort(nums, 0, nums.length - 1, temp);
        return nums; // Return the sorted array
    }

    /**
     * Recursively sorts the array using merge sort.
     *
     * @param nums the array to sort
     * @param left the starting index of the subarray
     * @param right the ending index of the subarray
     * @param temp temporary array for merging
     */
    private void mergesort(int[] nums, int left, int right, int[] temp) {
        if (left >= right) {
            return; // Base case: if the subarray has one or no elements, it's already sorted
        }

        // Calculate the midpoint of the subarray
        int mid = (left + right) / 2;

        // Recursively sort the two halves
        mergesort(nums, left, mid, temp);
        mergesort(nums, mid + 1, right, temp);

        // Merge the sorted halves
        merge(nums, left, mid, right, temp);
    }

    /**
     * Merges two sorted subarrays into a single sorted subarray.
     *
     * @param nums the array containing the subarrays
     * @param left the starting index of the first subarray
     * @param mid the ending index of the first subarray
     * @param right the ending index of the second subarray
     * @param temp temporary array for merging
     */
    private void merge(int[] nums, int left, int mid, int right, int[] temp) {
        int leftStart = left; // Starting index of the left subarray
        int rightStart = mid + 1; // Starting index of the right subarray

        // Number of elements in the left and right subarrays
        int leftSize = mid - left + 1;
        int rightSize = right - mid;

        // Copy the elements of the left and right subarrays into temp arrays
        for (int i = 0; i < leftSize; i++) {
            temp[leftStart + i] = nums[leftStart + i];
        }

        for (int i = 0; i < rightSize; i++) {
            temp[rightStart + i] = nums[rightStart + i];
        }

        int i = 0, j = 0, k = left;
        // Merge the temp arrays back into nums
        while (i < leftSize && j < rightSize) {
            if (temp[leftStart + i] <= temp[rightStart + j]) {
                nums[k] = temp[leftStart + i];
                i++;
            } else {
                nums[k] = temp[rightStart + j];
                j++;
            }
            k++;
        }

        // Copy remaining elements from the left subarray, if any
        while (i < leftSize) {
            nums[k] = temp[leftStart + i];
            i++;
            k++;
        }

        // Copy remaining elements from the right subarray, if any
        while (j < rightSize) {
            nums[k] = temp[rightStart + j];
            j++;
            k++;
        }
    }
}

