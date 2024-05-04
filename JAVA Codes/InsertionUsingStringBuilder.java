import java.util.*;

public class InsertionUsingStringBuilder {
    public static void main(String args[]) {
        StringBuilder sb = new StringBuilder("Tony");
        System.out.println(sb);
        // add S at the index 0
        sb.insert(0, 'S');
        System.out.print(sb);
    }
}
