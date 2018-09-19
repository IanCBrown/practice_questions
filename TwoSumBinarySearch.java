import java.util.Scanner; 
import java.util.Arrays; 

public class TwoSumBinarySearch {

    public static void main(String[] args) {
        int[] array = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
        59, 61, 67, 71, 73, 79, 83, 89, 97}; 

        Scanner scnr = new Scanner(System.in); 
        int userTarget = scnr.nextInt(); 

        TwoSumBinarySearch tsbs = new TwoSumBinarySearch(); 

        System.out.println(Arrays.toString(tsbs.twoSum(array, userTarget))); 
    }

    public int[] twoSum(int[] arr, int target) {
        
        for (int i = 0; i < arr.length - 1; i++) {
            int min = 0; 
            int max = arr.length - 1; 
            int firstSum = arr[i]; 
            int newTarget = target - firstSum; 
            while(min <= max) {
                int guess = (int)(max + min) / 2; 
                if (arr[guess] == newTarget) {
                    int[] retArr = {firstSum, newTarget}; 
                    return retArr; 
                } 
                else if (arr[guess] < newTarget) {
                    min = guess + 1; 
                } else {
                    max = guess - 1; 
                }
            }
        }
        int[] notFound = {-1, -1}; 
        return notFound; 
    }
}