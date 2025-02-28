# Next Permutation

## Problem Statement

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:  
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integers. More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation of that array is the permutation that follows it. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example:
- The next permutation of arr = [1,2,3] is [1,3,2].
- The next permutation of arr = [2,3,1] is [3,1,2].
- The next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographically larger rearrangement.

Given an array of integers nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.

## Classification

| Array Manipulation | Two Pointers |
|--------------------|--------------|

## Input Format

- **nums:** A list of integers representing the permutation.

## Constraints

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

## Critical Edge Cases

| Input                  | Expected Output |
|------------------------|-----------------|
| [1,2,3]                | [1,3,2]       |
| [3,2,1]                | [1,2,3]       |
| [1,1,5]                | [1,5,1]       |

## Approaches

| Approach                     | Time Complexity | Space Complexity | Data Structures           |
|------------------------------|-----------------|------------------|---------------------------|
| Brute Force (Next Permutation Generation) | O(n!)           | O(n)             | Array, Permutations       |
| Efficient In-Place Swap and Reverse         | O(n)            | O(1)             | Array, Two Pointers       |

## Final Code Reference

[Java Code](./LeetCode31.java)
[Python Code](./LeetCode31.py)
