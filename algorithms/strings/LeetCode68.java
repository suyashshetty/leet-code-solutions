package algorithms.strings;

import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode Problem 68
 * Level: Hard
 * Title: Text Justification
 * 
 * Description:
 * Given an array of strings words and a width maxWidth, format the text such
 * that each line has exactly maxWidth characters and is fully (left and right)
 * justified.
 * 
 * You should pack your words in a greedy approach; that is, pack as many words
 * as you can in each line. Pad extra spaces ' ' when necessary so that each
 * line has exactly maxWidth characters.
 * 
 * Extra spaces between words should be distributed as evenly as possible. If
 * the number of spaces on a line does not divide evenly between words, the empty
 * slots on the left will be assigned more spaces than the slots on the right.
 * 
 * For the last line of text, it should be left-justified, and no extra space
 * is inserted between words.
 * 
 * Note:
 * A word is defined as a character sequence consisting of non-space characters
 * only. Each word's length is guaranteed to be greater than 0 and not exceed
 * maxWidth. The input array words contains at least one word.
 * 
 * Example 1:
 * 
 * Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
 * Output:
 * [
 *    "This    is    an",
 *    "example  of text",
 *    "justification.  "
 * ]
 */
class LeetCode68 {
    /**
     * Justifies the given list of words into fully justified text with the
     * specified maximum width.
     * 
     * @param words The list of words to be justified.
     * @param maxWidth The maximum width of each line after justification.
     * @return A list of fully justified strings.
     */
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int index = 0;

        while (index < words.length) {
            int totalChars = words[index].length();
            int last = index + 1;

            // Determine the last word index that can fit in the current line
            while (last < words.length) {
                // Check if adding the next word would exceed maxWidth
                if (totalChars + 1 + words[last].length() > maxWidth){
                    break;
                }
                totalChars += 1 + words[last].length();
                last++;
            }

            StringBuilder sb = new StringBuilder();
            sb.append(words[index]);
            int diff = last - index - 1;

            // If last line or only one word in the line, left-justify
            if (last == words.length || diff == 0) {
                for (int i = index + 1; i < last; i++) {
                    sb.append(" ");
                    sb.append(words[i]);
                }
                // Add trailing spaces to reach maxWidth
                for (int i = sb.length(); i < maxWidth; i++) {
                    sb.append(" ");
                }
            } else {
                // Middle justify
                // Calculate the number of spaces to distribute
                int spaces = (maxWidth - totalChars) / diff;
                int r = (maxWidth - totalChars) % diff;
                for (int i = index + 1; i < last; i++) {
                    // Distribute the extra spaces among the first few gaps
                    int numSpaces = (spaces + ((i - index - 1) < r ? 1 : 0));
                    for (int k = 0; k <= numSpaces; k++) {
                        sb.append(" ");
                    }
                    sb.append(words[i]);
                }
            }
            result.add(sb.toString());
            index = last;
        }
        return result;
    }
}
