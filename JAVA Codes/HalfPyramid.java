
import java.util.*;

public class HalfPyramid {
    public static void main(String[] args) {
        int l = 5;
        int b = 5;
        for (int i = 1; i <= l; i++) {
            for (int j = 1; j <= b; j++)
                if (j <= i) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            System.out.println();
        }
    }
}
