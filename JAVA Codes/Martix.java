import java.util.Scanner;

public class Martix {
    public static void main(String[] args) {
        Logic l = new Logic();
        System.out.println("Enter the elements of the first matrix:");
        int[][] matrix1 = l.getMatrix();
        System.out.println("Enter the elements of the second matrix:");
        int[][] matrix2 = l.getMatrix();

        l.addMatrix(matrix1, matrix2);
        l.subMatrix(matrix1, matrix2);
        l.multMatrix(matrix1, matrix2);
    }
}

class Logic {
    public int[][] getMatrix() {
        int[][] matrix = new int[2][2];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        return matrix;
    }

    public void addMatrix(int[][] A, int[][] B) {
        int[][] C = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        System.out.println("Addition of matrices:");
        displayMatrix(C);
    }

    public void subMatrix(int[][] A, int[][] B) {
        int[][] C = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                C[i][j] = A[i][j] - B[i][j];
            }
        }
        System.out.println("Subtraction of matrices:");
        displayMatrix(C);
    }

    public void multMatrix(int[][] A, int[][] B) {
        int[][] C = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                C[i][j] = 0;
                for (int k = 0; k < 2; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        System.out.println("Multiplication of matrices:");
        displayMatrix(C);
    }

    private void displayMatrix(int[][] matrix) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
