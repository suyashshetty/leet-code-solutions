# LeetCode 234: Palindrome Linked List

## Problem Statement

Given the head of a singly linked list, determine whether it is a palindrome.  
A palindrome linked list reads the same forward and backward.

### Example 1:
- **Input:** 1 -> 2 -> 2 -> 1
- **Output:** True

### Example 2:
- **Input:** 1 -> 2 -> 3 -> 4
- **Output:** False

## Classification

| Two Pointers | Linked List |
|--------------|-------------|

## Input Format

- **head:** Reference to the head of a singly-linked list.

## Constraints

- Number of nodes is in the range [0, 10^5].
- -10^5 <= Node.val <= 10^5

## Critical Edge Cases

| Input                           | Expected Output |
|---------------------------------|-----------------|
| Empty list                      | True            |
| Single element list (e.g., [1]) | True            |
| Standard palindrome             | True            |
| Non-palindrome list             | False           |

## Approaches

| Approach              | Time Complexity | Space Complexity | Data Structures         |
|-----------------------|-----------------|------------------|-------------------------|
| Reverse Second Half   | O(n)            | O(1)             | Linked List, Pointers   |
| Recursive             | O(n)            | O(n)             | Linked List             |

## Final Code Reference

[Source Code](./LeetCode234-PalindromeLinkedList.py)

## Memory Profiling and Test Cases

- Test Case 1: Simple Palindrome  
- Test Case 2: Not a Palindrome  
- Test Case 3: Single Element List  
- Test Case 4: Empty Linked List  
- Test Case 5: Large Palindrome List
