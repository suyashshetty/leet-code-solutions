# Insert Interval

## Problem Statement

You are given an array of non-overlapping intervals where intervals[i] = [starti, endi] represents the start and the end of the ith interval and the array is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and the end of another interval.

Insert newInterval into intervals such that intervals remains sorted in ascending order by starti and there are no overlapping intervals (merge overlapping intervals if necessary).

Return the intervals after the insertion.

*Note:* You don't need to modify intervals in-place. You can create a new array and return it.

## Classification

| Array | Intervals | Sorting | Merging |
|-------|-----------|---------|---------|

## Input Format

- **intervals:** A list of lists of integers, where each sub-list represents an interval as [start, end].
- **newInterval:** A list of two integers representing the interval to insert, formatted as [start, end].

## Constraints

- Intervals are non-overlapping.
- Intervals are sorted by their starting values.
- The newInterval can overlap with existing intervals.
- Merged intervals should have no overlapping.

## Critical Edge Cases

| Input                                                                                         | Expected Output             |
|-----------------------------------------------------------------------------------------------|-----------------------------|
| intervals = [[1,3],[6,9]], newInterval = [2,5]                                                | [[1,5],[6,9]]               |
| intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]                           | [[1,2],[3,10],[12,16]]       |
| intervals = [], newInterval = [5,7]                                                           | [[5,7]]                     |
| intervals = [[1,5]], newInterval = [2,3]                                                       | [[1,5]]                     |
| intervals = [[1,5]], newInterval = [2,7]                                                       | [[1,7]]                     |

## Approaches

| Approach                     | Time Complexity | Space Complexity | Data Structures           |
|------------------------------|-----------------|------------------|---------------------------|
| Insert then Merge            | O(n)            | O(n)             | Array                     |
| Binary Search + Merge        | O(n)            | O(n)             | Array, Binary Search      |

## Final Code Reference

[Source Code](./InsertInterval.py)
