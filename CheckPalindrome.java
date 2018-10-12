import java.util.Scanner; 
import java.util.Arrays; 

public class CheckPalindrome {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in); 
        String palindrome_candidate = n.nextLine(); 
        System.out.println(checkPalindrome(palindrome_candidate)); 
    }

    static boolean checkPalindrome(String inputString) {
        char[] left_to_right = inputString.toCharArray();
        char[] right_to_left = new char[inputString.length()];

        int j = 0;
        for (int i = inputString.length() - 1; i >= 0; i--) {
            right_to_left[j] = left_to_right[i];
            j++; 
        }

        System.out.println(right_to_left);
        if (Arrays.equals(left_to_right, right_to_left)) {
            return true; 
        }
        else {
            return false; 
        }
    }
}