import java.util.Arrays;
import java.util.Scanner;

public class autori {

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in); 
        String text = input.nextLine(); 

        String[] arr = text.split("\\-"); 

        for (String item : arr) {
            System.out.print(item.toCharArray()[0]); 
        }

        System.out.println(); 
    }
}