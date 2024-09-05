**Problem Statement**

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of 
arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

**Explanation:**

The goal is to rearrange the array into the lexicographically next permutation. 
If no such permutation exists, we return the array sorted in ascending order.

**Steps:**
Find the first decreasing element: Traverse the array from the right to find the 
first element nums[i] that is smaller than nums[i + 1]. This is where the permutation 
can be adjusted to get the next permutation.

Find the element to swap with: After identifying i, find the smallest element to the right 
of i that is larger than nums[i]. Swap these two elements to ensure we move to 
the next larger permutation.

Reverse the sequence: To get the next permutation, reverse the sequence after index i to 
get the smallest lexicographical order for that part of the array.

**Time Complexity:**
O(n), where n is the number of elements in the array. This is because we perform three linear 
scans of the array (finding the first decreasing element, finding the element to swap, and reversing the subarray).

**Space Complexity:**
O(1), as the problem requires in-place rearrangement and we only use constant extra memory.




### Steps:
1. **Find the first decreasing element**:
   - Index `i = 1`, `nums[i] = 2`
   
2. **Find the element to swap**:
   - Swap `nums[1]` and `nums[2]` → `[1, 3, 2]`
   
3. **Reverse the subarray**:
   - No need to reverse further as there's only one element left.

#### Final Output: [1, 3, 2]
