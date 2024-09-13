package algorithms.strings;

/**
 * LeetCode Problem 2697
 * Level: Easy
 * Title: Lexicographically Smallest Palindrome
 * 
 * Description:
 * You are given a string s consisting of lowercase English letters, and
 * you are allowed to perform operations on it. In one operation, you can
 * replace a character in s with another lowercase English letter.
 * 
 * Your task is to make s a palindrome with the minimum number of operations
 * possible. If there are multiple palindromes that can be made using the
 * minimum number of operations, make the lexicographically smallest one.
 * 
 * A string a is lexicographically smaller than a string b (of the same length)
 * if in the first position where a and b differ, string a has a letter that
 * appears earlier in the alphabet than the corresponding letter in b.
 * 
 * Return the resulting palindrome string.
 * 
 * Example 1:
 * 
 * Input: s = "egcfe"
 * Output: "efcfe"
 * Explanation: The minimum number of operations to make "egcfe" a palindrome
 * is 1, and the lexicographically smallest palindrome string we can get by
 * modifying one character is "efcfe", by changing 'g'.
 * 
 * For more information, visit:
 * https://leetcode.com/problems/lexicographically-smallest-palindrome/
 */
public class LeetCode2697 {
    /**
     * Converts a string to the smallest lexicographical palindrome.
     * 
     * @param s The input string.
     * @return The smallest lexicographical palindrome that can be made from the input string.
     * 
     */
    public String makeSmallestPalindrome(final String s) {
        final char str[] = s.toCharArray();
        int i = 0, j = s.length() - 1;

        while (i < j) {
            // Set both str[i] and str[j] to the smaller of the two to ensure
            // the smallest lexicographical palindrome
            str[i] = (char) Math.min(str[i], str[j]);
            str[j--] = str[i++];
        }

        return new String(str);
    }
}
