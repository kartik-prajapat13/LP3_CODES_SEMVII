import java.util.Scanner;

public class fibo_both {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the position of the Fibonacci number: ");
        int n = scanner.nextInt();

        System.out.print("Choose method (1 for Iterative, 2 for Recursive): ");
        int choice = scanner.nextInt();

        scanner.close();

        int[] result;
        if (choice == 1) {
            result = calculateFibonacciIterative(n);
        } else {
            result = calculateFibonacciRecursive(n);
        }

        System.out.println("The " + n + "th Fibonacci number is: " + result[0]);
        System.out.println("Total steps taken: " + result[1]);
    }

    // Non-Recursive (Iterative) Fibonacci
    public static int[] calculateFibonacciIterative(int n) {
        if (n == 0)
            return new int[] { 0, 0 };
        if (n == 1)
            return new int[] { 1, 0 };

        int a = 0;
        int b = 1;
        int fibNumber = 0;
        int stepCount = 0;

        for (int i = 2; i <= n; i++) {
            fibNumber = a + b;
            a = b;
            b = fibNumber;
            stepCount++; // Increment step count for each addition
        }

        return new int[] { fibNumber, stepCount };
    }

    // Recursive Fibonacci with step counting
    public static int[] calculateFibonacciRecursive(int n) {
        int[] stepCount = { 0 };
        int fibNumber = fibonacciRecursiveHelper(n, stepCount);
        return new int[] { fibNumber, stepCount[0] };
    }

    private static int fibonacciRecursiveHelper(int n, int[] stepCount) {
        stepCount[0]++; // Increment step count for each recursive call
        if (n == 0)
            return 0;
        if (n == 1)
            return 1;
        return fibonacciRecursiveHelper(n - 1, stepCount) + fibonacciRecursiveHelper(n - 2, stepCount);
    }
}
