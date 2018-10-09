import java.util.Scanner;

public class alphabet_spam {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        String input = scnr.nextLine();
        scnr.close();

        ratios(input);
    }

    public static void ratios(String string_in) {
        int whitespace_count = 0;
        int lower_count = 0;
        int upper_count = 0; 
        int symbol_count = 0; 
        int len = string_in.length();

        char[] str_arr = string_in.toCharArray();

        for (char letter : str_arr) {
            if (letter == 95) {
                whitespace_count++; 
            }
            else if (letter >= 97 && letter <= 122) {
                lower_count++; 
            }
            else if (letter >= 65 && letter <= 90) {
                upper_count++; 
            }
            else {
                symbol_count++; 
            }
        }

        System.out.println((double) whitespace_count / len);
        System.out.println((double) lower_count / len); 
        System.out.println((double) upper_count / len); 
        System.out.println((double) symbol_count / len); 
    }

}
