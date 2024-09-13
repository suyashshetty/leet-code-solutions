
## 3217. Delete Nodes From Linked List Present in Array

#### LeetCode Problem 3217
#### Level: Medium
#### Link : https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/


### Description
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

### Example 1

**Input:** `nums = [1,2,3]`, `head = [1,2,3,4,5]`

**Output:** `[4,5]`

## Solution

The most efficient solution for this problem is as follows:

Steps:
1. Create a HashSet from the `nums` array for efficient lookup.
2. Traverse the linked list:
    - If the current node's value exists in the HashSet, skip the node by adjusting the pointers.
    - Otherwise, keep the node in the modified list.
3. Return the modified linked list.

**Time Complexity**: O(n + m), where n is the size of `nums` and m is the number of nodes in the linked list.

**Space Complexity**: O(n), for the HashSet.
