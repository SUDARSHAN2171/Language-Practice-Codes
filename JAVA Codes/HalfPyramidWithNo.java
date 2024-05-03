import java.util.*;

public class HalfPyramidWithNo {
    public static void main(String[] args) {
        int l = 5;
        for (int i = 1; i <= l; i++) {
            for (int j = 1; j <= i; j++) {
                if (i >= j) {
                    System.out.print(j);
                } else {
                    System.out.print(" ");
                }

            }
            System.out.println();
        }
    }
}