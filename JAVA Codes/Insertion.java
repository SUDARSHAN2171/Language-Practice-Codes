import java.util.*;

public class Insertion {
    public static void prarr(int arr[]) {
        System.out.print("Your Sorted array : ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your array size : ");
        int size = sc.nextInt();
        System.out.print("Enter the elemets in array : ");
        int array[] = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = sc.nextInt();
        }
        for (int i = 1; i < array.length; i++) {
            int current = array[i];
            int j = i - 1;
            while (j >= 0 && current < array[j]) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = current;
        }
        prarr(array);
    }
}