# Combination Sum IV

## Problem Statement

Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

*Note:* The test cases are generated so that the answer can fit in a 32-bit integer.

## Classification

| Array | Dynamic Programming | Combinatorics | Backtracking/Memoization |
|-------|---------------------|---------------|--------------------------|

## Input Format

- **nums:** A list of distinct integers.
- **target:** An integer representing the target sum.

## Constraints

- All numbers in `nums` are distinct.
- The order of the numbers matters in the combination.
- The answer is guaranteed to fit within a 32-bit integer.

## Critical Edge Cases

| Input                               | Expected Output |
|-------------------------------------|-----------------|
| nums = [1, 2, 3], target = 4         | 7               |
| nums = [9], target = 3               | 0               |
| nums = [1], target = 1               | 1               |

## Approaches

| Approach                           | Time Complexity | Space Complexity | Data Structures          |
|------------------------------------|-----------------|------------------|--------------------------|
| Dynamic Programming (Bottom-Up)    | O(n * target)   | O(target)        | Array                    |
| Backtracking with Memoization      | O(n * target)   | O(target)        | Recursion Stack, Dictionary |
