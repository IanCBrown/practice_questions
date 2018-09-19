import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

// every letter in the alphabet has a number value starting at a = 1; 
// every words has some value equal to the sum of these letter values. 
// compare words for equality based on these sums. 
public class FalseEquivalence {


  public static char[] alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                    'q','r','s','t','u','v','w','x','y','z'};

  public static ArrayList<Integer> totals = new ArrayList<Integer>();
  public static void main(String[] args) {
    Scanner scnr = new Scanner(System.in).useDelimiter(" ");

    while (scnr.hasNext()) {
      String input = scnr.next().toLowerCase();
      FalseEquivalence.getValues(input);
    }

    if (FalseEquivalence.isEquivalent()) {
      System.out.println("Equivalent");
    }
    else {
      System.out.println("Not equivalent");
    }
  }

  public static void getValues(String input) {

  ArrayList<Integer> matches = new ArrayList<Integer>();

    for (char c : input.toCharArray()) {
      for (int i = 0; i < alphabet.length; i++) {
        if (c == alphabet[i]) {
          matches.add(i + 1);
        }
      }
    }

    int total = 0;
    for (int i = 0; i < matches.size(); i++) {
      total += matches.get(i);
    }
    totals.add(total);
  }

  public static boolean isEquivalent() {
    if (totals.get(0) == totals.get(1)) {
      return true;
    }
    return false;
  }

}
