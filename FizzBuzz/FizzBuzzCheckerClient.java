import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.lang.StringBuilder;
import java.util.Arrays;


public class FizzBuzzCheckerClient {

   public static void main(String[] args) throws FileNotFoundException {
      FizzBuzzChecker fbChecker = new FizzBuzzChecker(new FileInputStream(new File("ResultsFizzBuzz.txt")));
   
      fbChecker.isCorrect();
   
      for (Boolean b : fbChecker.truthTable) {
         System.out.println(b);
      }
   }
}
