import java.util.*;

public class ReverseHalfPyramid {
    public static void main(String args[]) {
        int l = 4;
        int b = 4;
        for (int i = 1; i <= l; i++) {
            for (int j = 1; j <= b; j++) {
                if (i + j <= 5) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
