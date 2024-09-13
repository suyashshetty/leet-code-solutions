# Leetcode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

## Problem Description

Given an array of integers `nums` and an integer `limit`, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`.

## Example

Input: `nums = [8,2,4,7], limit = 4`

Output: `2`

Explanation: The subarray `[2,4]` has absolute difference `4` which is less than or equal to the limit.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`


## Approach

To solve this problem, we can use a sliding window approach. 

We will maintain two pointers, `left` and `right`, which represent the start and end of the current subarray. We will also maintain a `minHeap` and a `maxHeap` to keep track of the minimum and maximum elements in the current subarray.

Initially, both `left` and `right` will be set to 0. We will iterate through the array using the `right` pointer and expand the subarray until the absolute difference between the maximum and minimum elements in the subarray is greater than `limit`. 

If the absolute difference exceeds the limit, we will increment the `left` pointer and remove the corresponding element from the heaps until the condition is satisfied again.

At each step, we will update the length of the longest subarray if necessary.

Finally, we will return the length of the longest subarray as the result.

The time complexity of this approach is O(n log n), where n is the length of the input array `nums`, due to the operations performed on the heaps.

## Time Complexity
The time complexity of the sliding window approach described above is O(n log n), where n is the length of the input array `nums`. This is because for each element in the array, we perform operations on the heaps, which have a time complexity of O(log n) for insertion and removal. Since we iterate through the entire array once, the overall time complexity is O(n log n).

## Space Complexity
The space complexity of this approach is O(n), where n is the length of the input array `nums`. This is because we use two heaps, `minHeap` and `maxHeap`, to keep track of the minimum and maximum elements in the current subarray. The size of these heaps can grow up to the size of the input array, resulting in a space complexity of O(n).

