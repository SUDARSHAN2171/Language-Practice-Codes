import java.util.*;

public class OddNumberDetection {
    public static void oddno(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 != 0) {
                sum = sum + i;
            }
        }
        System.out.println(sum);
        return;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your nth no.:");
        int n = sc.nextInt();
        oddno(n);
    }
}
