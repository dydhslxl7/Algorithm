package baekjoon;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());
        String str = in.nextLine();

        int total = 0;
        for (int i = 0; i < n; i++) {
            total += (str.charAt(i) - 48);
        }

        System.out.println(total);
        in.close();
    }
}
