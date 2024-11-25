import java.util.Scanner;

public class cookies {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int c = scan.nextInt();

        if (n % c == 0) {System.out.print("YES");}
        else {System.out.print("NO");}
    }
}
a
