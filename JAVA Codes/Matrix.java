import java.util.*;

public class Matrix {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        int coloum = sc.nextInt();
        int matrix[][] = new int[row][coloum];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < coloum; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < coloum; j++) {
                System.out.println(matrix[row][coloum]);
            }
        }

    }
}
