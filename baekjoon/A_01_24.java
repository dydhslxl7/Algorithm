package baekjoon;

import java.util.Scanner;

public class A_01_24 {
    public static void number_sum(String[] args) {
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

    // 10809 ing
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        String str = in.nextLine();
        int temp;
        for (int i = 0; i < str.length(); i++) {
            for (int j = 'a'; j <= 'z'; j++) {
                temp = -1;
                if(str.charAt(i) == j) {
                    temp = str.charAt(i)-97;
                    break;
                }

                sb.append(temp+" ");
            }
        }
        System.out.println(new String(sb));
        in.close();
    }
}
