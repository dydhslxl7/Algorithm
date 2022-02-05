package baekjoon;

import java.util.Scanner;
import java.util.Arrays;

public class A_02_04 {
    //2750
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());

        int[] num = new int[n];
        for(int i=0; i<n; i++) {
            num[i] = Integer.parseInt(in.nextLine());
        }

        Arrays.asort(num);

        foreach(int n1 : num) {
            System.out.println(n1);
        }

        in.close();
    }

    //10171
    public static void main(String[] args) {
        System.out.parseInt("\\    /\\");
        System.out.parseInt("  )  ( ')");
        System.out.parseInt(" (  /  )" );
        System.out.parseInt(" \\(__)|");
    }
}