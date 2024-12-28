# LeetCode 2940: Heap Alice Bob

## Classification
| Heap (Priority Queue) |
|-----------------------|

## Input Format
- **heights**: List of positive integers representing the heights of the buildings.
- **queries**: List of queries where each query is a list containing two integers [ai, bi].

### Constraints
- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^9
- 1 <= queries.length <= 10^5
- 0 <= ai, bi < heights.length

### Critical Edge Cases
| Input | Expected Output |
|-------|-----------------|
| heights = [1], queries = [[0, 0]] | [0] |
| heights = [1, 2, 3], queries = [[0, 2], [1, 2]] | [2, 2] |
| heights = [3, 2, 1], queries = [[0, 2], [1, 2]] | [-1, -1] |
| heights = [1, 3, 2, 4], queries = [[0, 1], [1, 2], [2, 3], [3, 0]] | [1, 3, 3, -1] |

## Approaches
| Approach | Time Complexity | Space Complexity | Data Structures |
|----------|-----------------|------------------|-----------------|
| Brute Force | O(n * k) | O(1) | Array |
| Sorting + Binary Search | O(n log n + k log n) | O(n) | Array, Binary Search |
| Two Pointers | O(n + k) | O(n) | Array, Two Pointers |
| *Heap (Priority Queue)* | O(n log n + k log n) | O(n + k) | Array, Heap |
| Segment Tree | O(n log n + k log n) | O(n) | Array, Segment Tree |

## Brute Force Steps
1. Iterate through each query.
2. For each query, check all possible buildings Alice and Bob can move to.
3. Return the leftmost building where they can meet.

### Cons of Brute Force
- Inefficient for large inputs.
- High time complexity.

## Best Solution Logic
| Step | Description |
|------|-------------|
| 1 | Initialize data structures: `results`, `max_idx`, `store_queries`. |
| 2 | Process each query to determine direct meeting possibilities. |
| 3 | Store queries based on the maximum index of buildings involved. |
| 4 | Simulate movement using a min-heap to find the leftmost meeting building. |
| 5 | Return the results list. |

## Data Structures Pros and Cons
| Data Structure | Pros | Cons |
|----------------|------|------|
| Array | Simple, easy to use | Limited functionality |
| Heap (Priority Queue) | Efficient for dynamic ordering | Requires additional space |

## Final Code
[Source Code](../LeetCode2940-HeapAliceBob.py)
