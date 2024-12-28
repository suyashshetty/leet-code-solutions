package algorithms.trees.java;

/**
 * LeetCode Problem 124
 * Level: Medium
 * Title: Maximum Path Sum in a Binary Tree
 * 
 * A path in a binary tree is a sequence of nodes where each pair of 
 * adjacent nodes in the sequence has an edge connecting them. A node 
 * can only appear in the sequence at most once. Note that the path 
 * does not need to pass through the root.
 * 
 * The path sum of a path is the sum of the node's values in the path.
 * 
 * Given the root of a binary tree, return the maximum path sum of any 
 * non-empty path.
 * 
 * Example:
 * Input: [1, 2, 3]
 * Output: 6
 * Explanation: The maximum path sum is obtained by summing 2 -> 1 -> 3.
 */
public class LeetCode124 {

    /**
     * Finds the maximum path sum in the given binary tree.
     *
     * @param root the root of the binary tree
     * @return the maximum path sum
     */
    public int maxPathSum(TreeNode root) {
        // Stores the maximum path sum found so far
        int[] maxSum = new int[1];
        // Initialize with the smallest possible value
        maxSum[0] = Integer.MIN_VALUE;
        findMaxPath(root, maxSum);
        return maxSum[0];
    }

    /**
     * Helper method to recursively find the maximum path sum.
     *
     * @param node   the current node in the binary tree
     * @param maxSum array containing the global maximum path sum
     * @return the maximum path sum that includes the current node
     */
    private int findMaxPath(TreeNode node, int[] maxSum) {
        if (node == null) {
            // Base case: return 0 for null nodes
            return 0;
        }

        // Recursively find the maximum sum on the left and right subtrees
        // Ignore negative sums
        int leftSum = Math.max(0, findMaxPath(node.left, maxSum));
        // Ignore negative sums
        int rightSum = Math.max(0, findMaxPath(node.right, maxSum));

        // Calculate the maximum sum including the current node
        int currentMax = node.val + leftSum + rightSum;

        // Update the global maximum sum if currentMax is greater
        maxSum[0] = Math.max(maxSum[0], currentMax);

        // Return the maximum sum of the path that can be extended to the 
        // parent node
        return node.val + Math.max(leftSum, rightSum);
    }

    /**
     * Definition for a binary tree node.
     */
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }
}
