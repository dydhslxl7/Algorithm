package baekjoon;

import java.util.Scanner;

public class A_01_25 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(in.nextLine());

        int n2;
        String str;
        for (int i = 0; i < n; i++) {
            str = in.nextLine();
            n2 = str.charAt(0) - '0';
            str = str.substring(2);
            
            for (int j = 0; j < str.length(); j++) {
                for (int j2 = 0; j2 < n2; j2++) {
                    sb.append(str.charAt(j));
                }
            }
            sb.append("\n");
        }

        System.out.println(new String(sb));
    }
}
