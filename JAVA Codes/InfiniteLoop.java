import java.util.*;

public class InfiniteLoop {
    public static void loop(int i) {
        int a = 1;
        do {
            System.out.print(i);
            i++;
        } while (i > a);
        return;
    }

    public static void amin(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        loop(i);
    }
}
