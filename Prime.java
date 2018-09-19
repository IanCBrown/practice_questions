// prime number
// easy interview question
import java.util.Scanner;

public class Prime {

	public static void main(String[] args) {
		Scanner userPrime = new Scanner(System.in);
		System.out.print("Prints all primes below this number: ");
		int bound = userPrime.nextInt();
		for (int i = 0; i < bound; i++) {
			if (isPrime(i)) {
				System.out.println(i);
			}
		}
	}

	public static boolean isPrime(int n) {
		for (int i = 2; i < n; i++) {
			if (n % i == 0) {
				return false;
			}
		}
		return true;
	}

}
