package algorithms.linkedlist.java.leetcode3217;

import java.util.HashSet;
import java.util.Set;

public class LeetCode3217 {

    public ListNode modifiedList(int[] nums, ListNode head) {

        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        ListNode dummy = new ListNode(0);  // Dummy node to handle head removal easily
        dummy.next = head;
        ListNode current = dummy;

        while (current.next != null) {
            if (numSet.contains(current.next.val)) {
                current.next = current.next.next;  // Remove the node
            } else {
                current = current.next;
            }
        }

        return dummy.next;
    }
}
