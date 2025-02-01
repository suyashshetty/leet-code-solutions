"""
You are given an array of length n which was originally sorted in ascending 
order. It has now been rotated between 1 and n times. For example, the array 
nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of 
target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique.

A solution that runs in O(n) time is trivial, can you write an algorithm that 
runs in O(log n) time?
"""

from typing import List

class SearchInSortedRotatedArray:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # If we've found the target, return its index.
            if nums[mid] == target:
                return mid
            
            # Determine if the left half is sorted.
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Otherwise, the right half must be sorted.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # Target not found.
        return -1

# Example usage:
if __name__ == "__main__":
    sol = SearchInSortedRotatedArray()
    nums = [4, 5, 6, 7, 0, 1, 2]  # Example rotated sorted array
    print("Index of target {} is: {}".format(6, sol.search(nums, 6)))
    print("Index of target {} is: {}".format(10, sol.search(nums, 10)))
