import java.util.Scanner;
import java.util.ArrayList;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FizzBuzzChecker {

   public ArrayList<String> FizzBuzzArr = new ArrayList<String>();
   public ArrayList<Boolean> truthTable = new ArrayList<Boolean>();

   public FizzBuzzChecker(InputStream in) {
      try {
         Scanner scnr = new Scanner(new BufferedReader(new InputStreamReader(in)));
      
         while (scnr.hasNext()) {
            String str = scnr.nextLine();
         
            FizzBuzzArr.add(str.toLowerCase());
         }
         in.close();
      }
      catch (java.io.IOException e) {
         System.err.println("Error reading from InputStream.");
         System.exit(1);
      }
   }

   public void isCorrect() {
      for (int i = 0; i < FizzBuzzArr.size(); i++) {
         if (FizzBuzzArr.get(i).equals("fizz") && (i + 1) % 3 == 0) {
            truthTable.add(true);
         }
         else if (FizzBuzzArr.get(i).equals("buzz") && (i + 1) % 5 == 0) {
            truthTable.add(true);
         }
         else if (FizzBuzzArr.get(i).equals("fizzbuzz")
         && (i + 1) % 5 == 0
         && (i + 1) % 3 == 0) {
            truthTable.add(true);
         }
         else if (Pattern.matches("\\d+", FizzBuzzArr.get(i))) {
            truthTable.add(true);
         }
         else {
            truthTable.add(false);
         }
      }
   }

}
