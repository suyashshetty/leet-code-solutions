package algorithms.search;

public class LinearSearch{

    /**
     * Searches for the target value in the given array.
     *
     * @param input  the array to search in
     * @param target the value to search for
     * @return the index of the target value if found, otherwise -1
     */
    public int search(int[] input, int target) {
        if (input == null || input.length == 0) {
            return -1; // Return -1 for null or empty input array
        }

        int size = input.length;
        for (int i = 0; i < size; i++) {
            if (input[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
