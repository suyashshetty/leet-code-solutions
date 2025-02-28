# LeetCode 378: Kth Smallest Element in a Sorted Matrix

## Problem Statement

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix. Note that it is the kth smallest element in the sorted order, not the kth distinct element.

## Classification

| Heap (Priority Queue) | Binary Search |
|-------------------------|---------------|

## Input Format

- **matrix:** A list of lists of integers, where each sub-list represents a row of the matrix.
- **k:** An integer representing the kth smallest element to find.

## Constraints

- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
- 1 <= k <= n^2

## Critical Edge Cases

| Input                                                                                  | Expected Output |
|----------------------------------------------------------------------------------------|-----------------|
| matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8                                        | 13              |
| matrix = [[-5]], k = 1                                                                   | -5              |

## Approaches

| Approach                | Time Complexity   | Space Complexity | Data Structures             |
|-------------------------|-------------------|------------------|-----------------------------|
| Heap (Priority Queue)   | O(k log n)        | O(n)             | Heap, Matrix                |
| Binary Search           | O(n log(max - min)) | O(1)             | Binary Search, Matrix       |

## Final Code Reference

[Source Code](./leetcode378.py)
