package baekjoon;

import java.util.Scanner;

public class Main {
    //5622
    public static void dial(String[] args) {
        Scanner in = new Scanner(System.in);

        String str = in.nextLine();

        int c;
        int total = 0;
        for (int i = 0; i < str.length(); i++) {
            c = str.charAt(i) - 'A';
            if(c >= 0 && c < 3) {
                total += 3;
            } else if(c >= 3 && c < 6) {
                total += 4;
            } else if(c >= 6 && c < 9) {
                total += 5;
            } else if(c >= 9 && c < 12) {
                total += 6;
            } else if(c >= 12 && c < 15) {
                total += 7;
            } else if(c >= 15 && c < 19) {
                total += 8;
            } else if(c >= 19 && c < 22) {
                total += 9;
            } else {
                total += 10;
            }
        }

        System.out.println(total);

        in.close();
    }

    //2941
    public static void croatia(String[] args) {
        Scanner in = new Scanner(System.in);

        String str = in.nextLine();

        String[] al = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

        for (String s : al) {
            while(str.contains(s)) {
                str = str.replace(s, "!");
            }
        }

        System.out.println(str.length());
    }

    //1316 ing
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());

        String str;
        for (int i = 0; i < n; i++) {
            str = in.nextLine();

        }
    }
}
