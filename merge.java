import java.util.Arrays;

public class merge {

    public static void main(String[] args) {
        int[] ret; 
        int[] test_arr1 = {1,3,5,7}; 
        int[] test_arr2 = {2,4,6,8}; 
        
        ret = merge_arrays(test_arr1, test_arr2); 
        System.out.println(Arrays.toString(ret)); 
    }

    // merge two arrays, maintaining sorted order
    public static int[] merge_arrays(int[] arr1, int[] arr2) {
        int n1 = arr1.length;
        int n2 = arr2.length; 

        int[] ret_arr = new int[n1 + n2]; 

        int i, j, k;
        i = j = k = 0; 

        while (i < n1 && j < n2) {
            if (arr1[i] < arr2[j]) {
                ret_arr[k] = arr1[i];
                i++; 
            }
            else {
                ret_arr[k] = arr2[j]; 
                j++; 
            }
            k++; 
        }

        while (i < n1) {
            ret_arr[k] = arr1[i]; 
            i++; 
            k++; 
        }

        while (j < n2) {
            ret_arr[k] = arr2[j]; 
            j++; 
            k++; 
        }
        return ret_arr; 
    }


}