import java.util.Scanner; 

public class Complement {

    public static void main(String[] args) {
       Scanner scnr = new Scanner(System.in); 
       int uncomplemented = scnr.nextInt(); 
       scnr.close(); 
       byte x = 4;
       int y = 2;  
       System.out.println(~x); 
       System.out.println(Integer.toBinaryString(y)); 
       System.out.println(Integer.toBinaryString(~y));  

    }
}
