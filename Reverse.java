import java.util.Arrays;

public class Reverse {

    public static void main(String[] args) {
        String input = "Reverse this string"; 

        char[] work = input.toCharArray(); 
        int j = work.length - 1; 
        char temp; 
        for (int i = 0; i < work.length / 2; i++, j--) {
            temp = work[i]; 
            work[i] = work[j];
            work[j] = temp;
        }
 
        System.out.println(Arrays.toString(work)); 
        String ret = new String(work);
        System.out.println(ret); 
    }
}