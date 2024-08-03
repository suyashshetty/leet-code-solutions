package algorithms.greedy;

/**
 * LeetCode Problem 3068
 * Level: Hard
 * Title: Find the Maximum Sum of Node Values
 * 
 * Description:
 * There exists an undirected tree with n nodes numbered 0 to n - 1. You are 
 * given a 0-indexed 2D integer array edges of length n - 1, where edges[i] 
 * = [ui, vi] indicates that there is an edge between nodes ui and vi in the 
 * tree. You are also given a positive integer k, and a 0-indexed array of 
 * non-negative integers nums of length n, where nums[i] represents the value 
 * of the node numbered i.
 * 
 * Alice wants the sum of values of tree nodes to be maximum, for which Alice 
 * can perform the following operation any number of times (including zero):
 * Choose any edge [u, v] connecting the nodes u and v, and update their values 
 * as follows:
 * nums[u] = nums[u] XOR k
 * nums[v] = nums[v] XOR k
 * 
 * Return the maximum possible sum of the values Alice can achieve by performing 
 * the operation any number of times.
 */
public class Leetcode3068 {

    /**
     * Calculates the maximum possible sum of node values by performing XOR
     * operations.
     *
     * @param nums  the array of node values
     * @param k     the XOR value to be applied
     * @param edges the edges of the tree (not used in this method)
     * @return the maximum achievable sum
     */
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        int xorCount = 0; // Counts how many times the XOR operation improves the node value
        long totalSum = 0; // Accumulates the maximum sum
        int minDifference = Integer.MAX_VALUE; // Tracks the smallest difference between XOR and original value

        for (int num : nums) {
            int xorValue = num ^ k; // Compute XOR value
            if (xorValue > num) {
                totalSum += xorValue; // Add XOR value to totalSum if it is greater
                xorCount++; // Increment the count of improvements
            } else {
                totalSum += num; // Add original value to totalSum
            }

            // Update minDifference with the smallest absolute difference
            minDifference = Math.min(minDifference, Math.abs(xorValue - num));
        }

        // If the number of improvements is even, return the totalSum
        if (xorCount % 2 == 0) {
            return totalSum;
        }

        // If the number of improvements is odd, subtract the smallest difference to balance
        return totalSum - minDifference;
    }
}
