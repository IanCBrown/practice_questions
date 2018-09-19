import java.util.Random;

public class BinarySearch {

   public static void main(String[] args) {
      int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
         59, 61, 67, 71, 73, 79, 83, 89, 97}; 
      int target = 73; 

      int[] longArray = new int[100000000]; 
      int randTarget = randomFill(); 
      populateArray(longArray); 

      long startTimeBinary = System.currentTimeMillis(); 
      System.out.println(binarySearch(longArray, 120));
      long endTimeBinary = System.currentTimeMillis(); 
      System.out.println("Total execution time (binary): " + (endTimeBinary - startTimeBinary)); 
      System.out.println("///////////////////////"); 

      long startTimeLinear = System.currentTimeMillis(); 
      System.out.println(linearSearch(longArray, 120));  
      long endTimeLinear = System.currentTimeMillis(); 
      System.out.println("Total execution time (linear): " + (endTimeLinear - startTimeLinear)); 
   }

   public static int binarySearch(int[] array, int targetValue) {
      int min = 0; 
      int max = array.length - 1; 
      int guess;  
   
      while (min <= max) {
          guess = (int)((max + min) / 2);
         if (array[guess] == targetValue) {
            return array[guess]; 
         }
         else if (array[guess] < targetValue) {
            min = guess + 1; 
         }
         else {
            max = guess - 1; 
         }
      }
      return -1; 
   }

   public static int linearSearch(int[] array, int targetValue) {
       for (int i = 0; i < array.length; i++) {
           if (targetValue == array[i]) {
               return array[i]; 
           }
       }
       return -1; 
   }

   public static int randomFill() {
       Random rand = new Random(); 
       int randomNum = rand.nextInt(); 
       return randomNum; 
   }

   public static int[] populateArray(int[] array) {
       for (int i = 0; i < array.length; i++) {
           array[i] = i; 
       }
       return array; 
   }
}