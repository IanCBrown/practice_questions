import java.util.Scanner;

public class Panagram {

  public static void main(String[] args) {
    Scanner scnr = new Scanner(System.in);

    String input = scnr.nextLine().toLowerCase();

    if (Panagram.isPanagram(input)) {
      System.out.println("Is a Pangram!");
    }
    else {
      System.out.println("Is not a Pangram.");
    }
  }


  public static boolean isPanagram(String input) {

    if (input.contains("a") && input.contains("b") && input.contains("c") && input.contains("d") &&
    input.contains("e") && input.contains("f") && input.contains("g") &&
    input.contains("h") && input.contains("i") && input.contains("j") && input.contains("k") &&
    input.contains("l") && input.contains("m") && input.contains("n") &&
    input.contains("o") && input.contains("p") && input.contains("q") && input.contains("r") &&
    input.contains("s") && input.contains("t") && input.contains("u") && input.contains("v") &&
    input.contains("w") && input.contains("x") && input.contains("y") && input.contains("z")) {
      return true;
    }
    return false;
  }
}
