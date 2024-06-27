import java.util.*;

public class recursion {
    public static void print(int n) {
        if (n == 0) {
            return;
        }

        System.out.println(n);
        print(n - 1);
    }

    public static void main(String[] args) {
        Scanner number = new Scanner(System.in);
        System.out.println("Enter the You want to print reverse from : ");
        int num = number.nextInt();
        System.out.println("Reverse :");
        print(num);
    }
}
