import java.util.Arrays;

public class ArrayRemoval {
    public static void main(String[] args) {
        int[] test_arr = {1, 3, 4, 5, 6, 7, 43, 34, 66}; 

        System.out.println(Arrays.toString(test_arr));
        System.out.println(Arrays.equals(test_arr, test_arr2));

        test_arr = delete(test_arr, 1);

        System.out.println(Arrays.toString(test_arr));
    }

    public static int[] delete(int[] arr, int toBeDeleted) {
        int[] retArray = Arrays.copyOf(arr, arr.length - 1);
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == toBeDeleted) {
                for (int j = i; j < arr.length - 1; j++) {
                    retArray[j] = arr[j + 1];
                }
            }
        }
        return retArray;
    }
}
