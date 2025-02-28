package algorithms.arrays.leetcode57;
import java.util.Arrays;

/**
 * LeetCode Problem 57
 * Level: Medium
 * Title: Insert Interval
 * 
 * Description:
 * You are given an array of non-overlapping intervals intervals where
 * intervals[i] = [starti, endi] represent the start and the end of the
 * ith interval and intervals is sorted in ascending order by start(i).
 * You are also given an interval newInterval = [start, end] that 
 * represents the start and end of another interval.
 * 
 * Insert newInterval into intervals such that intervals is still sorted
 * in ascending order by starti and intervals still does not have any
 * overlapping intervals (merge overlapping intervals if necessary).
 * 
 * Return intervals after the insertion.
 * 
 * Note that you don't need to modify intervals in-place. You can make a
 * new array and return it.
 * 
 * Example 1:
 * 
 * Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
 * Output: [[1,5],[6,9]]
 */

class LeetCode57 {
    /**
     * Inserts a new interval into the list of intervals and merges any
     * overlapping intervals.
     * 
     * @param intervals The list of non-overlapping intervals sorted by start time.
     * @param newInterval The new interval to be inserted.
     * @return The list of intervals after inserting and merging the new interval.
     */
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;
        int[][] result = new int[n + 1][]; // Array to hold the result

        int i = 0, r = 0;
        boolean inserted = false; // Tracking if the new interval has been inserted.

        while (i < n) {
            // Current interval ends before the new interval starts
            if (intervals[i][1] < newInterval[0]) {
                result[r++] = intervals[i++];
            }
            // Current interval starts after the new interval ends
            else if (intervals[i][0] > newInterval[1]) {
                if (!inserted) {
                    result[r++] = newInterval; // Insert new interval
                    inserted = true;
                }
                result[r++] = intervals[i++]; // Add the current interval
            }
            // Overlapping intervals, merge them into the new interval
            else {
                newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
                newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
                i++;
            }
        }

        // Insert new interval if it hasn't been added yet
        if (!inserted) {
            result[r++] = newInterval;
        }

        // Return the merged intervals
        return Arrays.copyOf(result, r);
    }
}
