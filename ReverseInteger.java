public class ReverseInteger {

    public static void main(String[] args) {
      System.out.println(reverse(123456789));
    }

    //reverse method
    public static int reverse(int x) {
        int retVal = 0;
        if (x > Integer.MAX_VALUE || x < Integer.MIN_VALUE) {
          return retVal;
        }
        
        String numToString = Integer.toString(x);
        char[] reversed = new char[numToString.length()];
        String result = "";

        for (int i = numToString.length() - 1; i >= 0; i--) {
          result += numToString.charAt(i);
        }
        retVal = Integer.parseInt(result);
        return retVal;
    }
}
