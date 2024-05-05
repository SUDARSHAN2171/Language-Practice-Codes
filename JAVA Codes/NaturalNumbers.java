import java.util.*;

public class NaturalNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nth = sc.nextInt();
        int sum = 0;
        for (int i = 1; i <= nth; i++) {
            sum = sum + i;
        }
        System.out.println(sum);
    }
}