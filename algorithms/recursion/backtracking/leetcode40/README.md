# Combination Sum II

## Problem Statement

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

Return the list of all unique combinations. The solution set must not contain duplicate combinations.

## Classification

| Backtracking | Recursion | Sorting | Combinatorial |
|--------------|-----------|---------|---------------|

## Input Format

- **candidates:** A list of integers representing the candidate numbers.
- **target:** An integer representing the target sum.

## Constraints

- The same number may not be used more than once in a combination.
- The combination set should not include duplicate combinations.
- The input list may contain duplicates.
- It is recommended to sort the candidates to efficiently handle duplicates.

## Critical Edge Cases

| Input                                         | Expected Output              |
|-----------------------------------------------|------------------------------|
| candidates = [10,1,2,7,6,1,5], target = 8       | [[1,1,6],[1,2,5],[1,7],[2,6]] |
| candidates = [2,5,2,1,2], target = 5             | [[1,2,2], [5]]               |
| candidates = [], target = 3                      | []                           |
| candidates = [1], target = 2                     | []                           |

## Approaches

| Approach                         | Time Complexity   | Space Complexity | Data Structures       |
|----------------------------------|-------------------|------------------|-----------------------|
| Backtracking with Sorting        | O(2^n * n)        | O(n)             | Array, Recursion Stack|
| Depth-First Search (DFS)         | O(2^n * n)        | O(n)             | Array, Recursion Stack|
