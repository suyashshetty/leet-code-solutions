package algorithms.search;

public class LinearSearch{

    public int search(int[] input, int target) {
        int size = input.length;
        for(int i = 0; i < size; i++){
            if(input[i] == target){
                return i;
            }
        }
        return -1;
    }
    
}