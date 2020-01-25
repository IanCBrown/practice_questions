public class bottom_up_fib {
    public static void main(String[] args) {
        System.out.println(fib(10)); 
    }

    public static int fib(int n) {
        int new_fib = 0; 
        if (n == 0) {
            return 0; 
        }
        int prev_fib = 0, curr_fib = 1; 
        for (int i = 1; i < n; i++) {
            new_fib = prev_fib + curr_fib; 
            prev_fib = curr_fib; 
            curr_fib = new_fib; 
        }

        return curr_fib; 
    }
}